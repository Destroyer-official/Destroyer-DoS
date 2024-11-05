
---

<div align="center">

# 🌐 Destroyer-DoS: Advanced DDoS Simulation Tool 🌐

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)

</div>

---

<div align="center">

### 🚨⚠️ WARNING: Educational Purposes Only! Unauthorized Use May Have Legal Consequences. Act Responsibly and Obtain Proper Authorization. ⚠️🚨

</div>

---

### 📂 File: `ddos.py` - Destroyer Denial of Service Simulation

---

### 🌟 Overview

**Destroyer-DoS** is an educational script for simulating Distributed Denial of Service (DDoS) attacks. This tool uses Python’s async and multiprocessing capabilities to unleash high-impact network stress on specified IPs and ports. Ideal for testing network resilience in authorized environments. 🚀

---

### 🛠️ Features

- 🎯 **Multi-Protocol Support**: TCP, UDP, HTTP, HTTPS, ICMP
- 🚀 **Asynchronous Packet Sending**: Fast and non-blocking
- 🔄 **Multiprocessing**: High-throughput operations
- 🧩 **Flexible Packet Size, Process & Thread Control**
- 💻 **Cross-Platform Compatible** with Robust Error Handling

---

### 🚀 Installation & Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Destroyer-official/Destroyer-DoS.git
    ```

2. **Navigate to the Directory**:
    ```bash
    cd Destroyer-DoS
    ```

3. **Install Required Packages**:
   - Standard library dependencies are generally included with Python. If you're using Python <3.4, install any missing modules listed in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

---

### 🌐 Command Usage Examples

To execute the script, run:

```bash
python ddos.py -ip [Target_IP] -p [Target_Port] -pr [Processes] -t [Threads] -[Protocol]
```

Examples:

#### **Single Protocol Attack** 🌊
- **TCP Attack**:
    ```bash
    python ddos.py -ip 192.168.0.1 -p 80 -pr 30 -t 20 -T
    ```
- **UDP Attack**:
    ```bash
    python ddos.py -ip 192.168.0.1 -p 53 -pr 30 -t 20 -U
    ```
- **ICMP Ping Attack**:
    ```bash
    python ddos.py -ip 192.168.0.1 -pr 30 -t 20 -I
    ```
- **HTTP Flood**:
    ```bash
    python ddos.py -ip 192.168.0.1 -p 80 -pr 30 -t 20 -H
    ```
- **HTTPS Flood**:
    ```bash
    python ddos.py -ip 192.168.0.1 -p 443 -pr 30 -t 20 -S
    ```

#### **All Protocols Combined Attack** 🌐
- Run all protocols simultaneously:
    ```bash
    python ddos.py -ip 192.168.0.1 -p 80 -pr 30 -t 20 -A
    ```

#### **Advanced Options** ⚙️
- **Custom Port Range**:
    ```bash
    python ddos.py -ip 192.168.0.1 -p 80-90 -pr 30 -t 20 -T
    ```
- **Multiple Ports**:
    ```bash
    python ddos.py -ip 192.168.0.1 -p 80,443,8080 -pr 30 -t 20 -U
    ```
- **Specify Packet Size**:
    ```bash
    python ddos.py -ip 192.168.0.1 -p 80 -pr 30 -t 20 -ps 1024 -T
    ```

---

### 💻 Command-Line Arguments Guide

| Argument       | Description                                                                                       |
|----------------|---------------------------------------------------------------------------------------------------|
| `-ip`          | Target IP address.                                                                                |
| `-p`           | Target port (can be a single port, range, or multiple ports separated by commas).                 |
| `-T`           | Use TCP protocol for the test.                                                                    |
| `-U`           | Use UDP protocol for the test.                                                                    |
| `-I`           | Use ICMP protocol (ping simulation).                                                              |
| `-H`           | Use HTTP protocol.                                                                                |
| `-S`           | Use HTTPS protocol.                                                                               |
| `-A`           | Run all protocols concurrently.                                                                   |
| `-pr`          | Number of processes to run concurrently (default: 30).                                            |
| `-t`           | Number of threads per process (default: 40).                                                      |
| `-ps`          | Packet size in bytes (default: maximum for selected protocol).                                    |

---

### 📚 How It Works

1. **Target Preparation**:
   - Validates target IP and port information.
   - Establishes CPU affinity to optimize resource usage on multi-core systems.

2. **Protocol-Specific Packet Sending**:
   - **TCP**: Creates TCP connections and sends continuous random data streams.
   - **UDP**: Sends random UDP packets to impact network bandwidth.
   - **ICMP**: Simulates ping requests using ICMP packets.
   - **HTTP/HTTPS**: Sends asynchronous HTTP/HTTPS requests to simulate web server load.

3. **Process and Thread Management**:
   - Distributes load across multiple processes and threads, simulating distributed attacks.

---

### ⚠️ Disclaimer

**Disclaimer**: This script is intended for educational purposes only and should be used to test network robustness in authorized environments. Unauthorized use may have legal consequences. Always ensure proper authorization.

---

### 🤝 Contributing

Contributions are welcome! If you have ideas for improvements, feel free to submit a pull request or create an issue.

---

### 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

<div align="center">

Happy Testing! 🚀🌐

</div>

---

