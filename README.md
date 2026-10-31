# Basic Network Sniffer Using Python

## Project Overview

The Basic Network Sniffer is a Python-based cybersecurity project developed using the Scapy library. It captures and analyzes network packets in real time and displays important packet information such as source IP address, destination IP address, protocol, port numbers, timestamp, and packet length.

The project also provides protocol-based filtering and saves captured packet details into a CSV file for further analysis.

## Objectives

- Understand how network packets are transmitted.
- Capture live network traffic using Python.
- Identify common network protocols.
- Extract important packet information.
- Store captured packet details for analysis.

## Technologies Used

- **Programming Language:** Python 3.11
- **Library:** Scapy 2.8.0
- **Packet Capture Support:** Npcap
- **IDE:** Visual Studio Code
- **Operating System:** Windows

## Features

1. **All IP Packets:** Captures IPv4 packets.
2. **TCP Filtering:** Captures TCP packets only.
3. **UDP Filtering:** Captures UDP packets only.
4. **ICMP Filtering:** Captures ICMP packets only.
5. **Packet Analysis:** Displays source IP, destination IP, protocol, port numbers, timestamp, and packet length.
6. **CSV Logging:** Saves captured packet information into `captured_packets.csv`.
7. **Capture Summary:** Displays the total number of analyzed packets when capturing stops.

## Project Structure

```text
Basic-Network-Sniffer/
│
├── network_sniffer.py
├── captured_packets.csv
└── README.md
```

## Requirements

- Python 3.11 or later
- Scapy library
- Npcap installed on Windows

## Installation

Install Scapy using:

```bash
pip install scapy
```

Install Npcap from:

https://npcap.com/

## How to Run

1. Open the project folder in Visual Studio Code or PowerShell.
2. Run the following command:

```bash
python network_sniffer.py
```

3. Select one of the available options:

   - 1 – Capture all IP packets
   - 2 – Capture TCP packets only
   - 3 – Capture UDP packets only
   - 4 – Capture ICMP packets only

4. The program displays captured packet information in the terminal.
5. Press `Ctrl + C` to stop capturing.
6. Captured packet details are saved in `captured_packets.csv`.

## Packet Information Analyzed

| Field | Description |
|---|---|
| Timestamp | Time when the packet was captured |
| Source IP | IP address of the sender |
| Destination IP | IP address of the receiver |
| Protocol | TCP, UDP, ICMP, or Other IP |
| Source Port | Sender's port number, when applicable |
| Destination Port | Receiver's port number, when applicable |
| Packet Length | Size of the captured packet in bytes |

## Limitations

- The current implementation focuses on IPv4 packet analysis.
- Encrypted HTTPS payload data cannot be read as plain text.
- The project analyzes packet metadata and does not perform advanced intrusion detection.
- Packet capture depends on network permissions and Npcap configuration.

## Conclusion

This project demonstrates the basic working of a network sniffer using Python and Scapy. It provides practical experience in packet capturing, protocol identification, network traffic analysis, and CSV-based logging.

**Note:** This tool should only be used on networks where packet capture is authorized.
