<div align="center">

# 🌐 Destroyer-DoS 🌐

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)

</div>

<div align="center">

### 🚨⚠️ WARNING: For Educational Purposes Only! Unauthorized Use May Have Legal Consequences. Act Responsibly and Obtain Proper Authorization. ⚠️🚨

</div>

---

### 📂 File Name: `ddos.py` - Destroyer Denial of Service Script

---

### 🌟 Overview

🛡️ **Destroyer Denial of Service (DDoS) Script**: A powerful educational tool designed to simulate a Denial of Service (DoS) attack. Orchestrates an assault on a specified IP and port, unleashing a barrage of TCP packets. Utilizes Python's asyncio and multiprocessing for maximum impact. Deploy responsibly in authorized environments.

---

### 🛠️ Features

- 🎯 Flood a target IP with TCP packets.
- 🚀 Utilize asyncio for asynchronous packet transmission.
- 🔄 Leverage multiprocessing for concurrent execution.

---

### 🚀 Usage

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Destroyer-official/Destroyer-DoS.git
    ```

2. **Navigate to the directory:**
    ```bash
    cd Destroyer-DoS
    ```

---

3. **📦 Install the required packages:**
    - Required modules are part of the Python standard library and usually included with Python installations. No separate installation is needed.
 *Module included in the standard library:
       - socket
       - random
       - multiprocessing
       - argparse (since Python 3.2)

    For Python versions lower than 3.4.0:
    ```bash
    pip install -r requirements.txt
    ```
---

4. **✨ Execute the script using command-line arguments:**
    ```bash
    python ddos.py -ip [Target_IP] -p [Target_Port] -pr [Number_of_Processes] -t [Number_of_Threads per process] 
    ```
    ```bash
    python ddos.py -ip 192.168.0.1 -p 80 -pr 40 -t 20 
    ```

---

### 💻 Command-Line Arguments

- `-ip`: Specify the target IP address.
- `-p`: Define the target port number.
- `-pr`: Set the number of processes to run concurrently (default: 30).
- `-t`: Define the number of threads per process (default: 40).

---

### 📚 How It Works

1. **IP Info Gathering:**
   - Resolves the target hostname.
   - Initiates asynchronous packet sending tasks.

2. **Packet Sending:**
   - Establishes a TCP connection to the target IP and port.
   - Sends a continuous stream of random data.

---

### 📜 Disclaimer

⚠️ **Disclaimer**: This script is exclusively designed for educational purposes. Unauthorized or inappropriate use may result in legal consequences. Exercise caution and ensure proper authorization.

---

### 🤝 Contributing

🤝 Contributions are welcome! For suggestions, enhancements, or issues, feel free to create a pull request or submit an issue in the repository.

---

### 📜 License

⚖️ This project is licensed under the MIT License. Refer to the [LICENSE](LICENSE) file for detailed licensing information.

<div align="center">

---

</div>
