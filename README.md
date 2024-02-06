<div align="center">

# 🌐 Destroyer-DoS 🌐
 <div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)

</div>

<div align="center">

### 🚨⚠️ WARNING: For Educational Purposes Only! Unauthorized Use May Have Legal Consequences. Act Responsibly and Obtain Proper Authorization. ⚠️🚨

</div>

---

### 📂 File Name: `ddos.py` - Destroyer Denial of Service Script
## Disclaimer

---
**IMPORTANT:** Password cracking, even for educational purposes, can be risky and may violate ethical or legal standards. Always respect copyright and digital rights. Exercise caution and ensure you have the necessary permissions before attempting to crack any PDF passwords. This script is intended for educational use only to demonstrate parallel processing and password cracking techniques. It is not intended for malicious or unauthorized use.

### 🌟 Overview
## Overview

🛡️ **Destroyer Denial of Service (DDoS) Script**: A powerful educational tool designed to simulate a Denial of Service (DoS) attack. Orchestrates an assault on a specified IP and port, unleashing a barrage of TCP packets. Utilizes Python's asyncio and multiprocessing for maximum impact. Deploy responsibly in authorized environments.
The Parallel PDF Password Cracker utilizes parallel processing to explore password cracking techniques in a controlled educational environment. This Python script maximizes CPU utilization to accelerate password cracking attempts on encrypted PDF files.

---
## Project Structure

### 🛠️ Features
```
.
├── pdf_cracker.py
├── README.md
├── requirements.txt
└── ...
```

- 🎯 Flood a target IP with TCP packets.
- 🚀 Utilize asyncio for asynchronous packet transmission.
- 🔄 Leverage multiprocessing for concurrent execution.
## Features

---
- **Parallel Processing:** Leverages multiprocessing and multithreading for faster password cracking.
- **Customizable Options:** Fine-tune chunk size, process count, and thread count for optimal performance.
- **User-friendly Interface:** Interact with the script seamlessly through a clear command-line interface.
- **Error Handling:** Handles common file-related errors gracefully.
- **Logging:** Provides detailed records for debugging and analysis.

### 🚀 Usage
## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Destroyer-official/Destroyer-DoS.git
    git clone https://github.com/Destroyer-official/EthicalPDFCracker.git
    ```

2. **Navigate to the directory:**

    ```bash
    cd Destroyer-DoS
    cd EthicalPDFCracker
    ```

---

3. **📦 Install the required packages:**
    - Required modules are part of the Python standard library and usually included with Python installations. No separate installation is needed.
 *Module included in the standard library:
       - socket
       - random
       - multiprocessing
       - argparse (since Python 3.2)
3. **Install the required packages:**

    For Python versions lower than 3.4.0:
    ```bash
    pip install -r requirements.txt
    ```
---

4. **✨ Execute the script using command-line arguments:**
    ```bash
    python ddos.py -ip [Target_IP] -p [Target_Port] -pr [Number_of_Processes] -t [Number_of_Threads per process] 
    ```
4. **Execute the script:**

    ```bash
    python ddos.py -ip 192.168.0.1 -p 80 -pr 40 -t 20 
    python pdf_cracker.py -pdf <path_to_pdf_file> -pass <path_to_password_list>
    ```

---
## Optional Arguments

### 💻 Command-Line Arguments
- `-ch`: Size of password chunks for parallel processing (default: 10000).
- `-pr`: Number of parallel processes (default: 50).
- `-thr`: Number of threads per process (default: 20).

- `-ip`: Specify the target IP address.
- `-p`: Define the target port number.
- `-pr`: Set the number of processes to run concurrently (default: 30).
- `-t`: Define the number of threads per process (default: 40).
**Example Usage:**

---
```bash
python pdf_cracker.py -pdf encrypted_file.pdf -pass passwords.txt -ch 10000 -pr 50 -thr 20
```

### 📚 How It Works
## How It Works

1. **IP Info Gathering:**
   - Resolves the target hostname.
   - Initiates asynchronous packet sending tasks.
The `pdf_cracker.py` script is designed to efficiently crack the password of encrypted PDF files by leveraging parallel processing. Here's a breakdown of its key components and functionality:

2. **Packet Sending:**
   - Establishes a TCP connection to the target IP and port.
   - Sends a continuous stream of random data.
1. **🔐 Password Decryption Attempt:**
    - The script attempts to decrypt the PDF file using a list of passwords provided in the specified password list file.

---
2. **⚡ Parallel Processing:**
    - To expedite the cracking process, the script utilizes multiprocessing to parallelize password attempts. Each chunk of passwords is processed concurrently, making the most out of the available CPU cores.

### 📜 Disclaimer
3. **🔄 Multithreading:**
    - Within each process, multithreading is employed to further optimize performance. This allows multiple password attempts to be made simultaneously within a process.

⚠️ **Disclaimer**: This script is exclusively designed for educational purposes. Unauthorized or inappropriate use may result in legal consequences. Exercise caution and ensure proper authorization.
4. **🍱 Chunked Passwords:**
    - Passwords are divided into chunks based on the specified chunk size. This allows for efficient distribution of password attempts across multiple processes.

---
5. **⚠️ Error Handling:**
    - The script incorporates robust error handling to gracefully manage common file-related errors. Any exceptions encountered during the decryption attempts are logged for further analysis.

### 🤝 Contributing
6. **📝 Logging:**
    - Detailed logs are generated to record important events during the password cracking process. This includes information about successful password attempts or encountered errors.

🤝 Contributions are welcome! For suggestions, enhancements, or issues, feel free to create a pull request or submit an issue in the repository.
7. **⚙️ Customizable Options:**
    - Users have the flexibility to customize the chunk size, number of parallel processes, and number of threads per process through command-line arguments. This ensures adaptability to different hardware configurations.

---
8. **🚪 Exit Upon Success:**
    - As soon as the correct password is found, the script exits, and the correct password is displayed. This minimizes unnecessary processing once the goal is achieved.

### 📜 License
9. **🎓 Educational Purpose Emphasis:**
    - The script is developed strictly for educational purposes and is intended to showcase the principles of parallel processing in the context of password cracking. Users are reminded to use the script responsibly and adhere to ethical and legal standards.

⚖️ This project is licensed under the MIT License. Refer to the [LICENSE](LICENSE) file for detailed licensing information.
By understanding these key components, users can gain insights into the inner workings of the script and appreciate the efficiency achieved through parallel processing for password cracking.

<div align="center">
## Contributing

---
Contributions are welcome! Fork the repository, make your enhancements, and create a pull request.

</div>
### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
