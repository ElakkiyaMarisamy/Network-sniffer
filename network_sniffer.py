
import csv
from datetime import datetime
from scapy.all import sniff, IP, TCP, UDP, ICMP

packet_count = 0
log_file = "captured_packets.csv"


def analyze_packet(packet):
    global packet_count

    if IP not in packet:
        return

    packet_count += 1

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst
    packet_length = len(packet)

    timestamp = datetime.fromtimestamp(
        float(packet.time)
    ).strftime("%Y-%m-%d %H:%M:%S")

    if TCP in packet:
        protocol = "TCP"
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport

    elif UDP in packet:
        protocol = "UDP"
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport

    elif ICMP in packet:
        protocol = "ICMP"
        source_port = "-"
        destination_port = "-"

    else:
        protocol = "Other IP"
        source_port = "-"
        destination_port = "-"

    print(f"\nPacket #{packet_count}")
    print("Timestamp       :", timestamp)
    print("Source IP       :", source_ip)
    print("Destination IP  :", destination_ip)
    print("Protocol        :", protocol)
    print("Source Port     :", source_port)
    print("Destination Port:", destination_port)
    print("Packet Length   :", packet_length, "bytes")
    print("-" * 45)

    # Save packet details to CSV
    with open(log_file, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            packet_count,
            timestamp,
            source_ip,
            destination_ip,
            protocol,
            source_port,
            destination_port,
            packet_length
        ])


def start_sniffer():
    print("\nPYTHON NETWORK SNIFFER")
    print("=" * 35)
    print("1. Capture all IP packets")
    print("2. Capture TCP packets only")
    print("3. Capture UDP packets only")
    print("4. Capture ICMP packets only")

    choice = input("\nChoose an option (1-4): ")

    filters = {
        "1": None,
        "2": "tcp",
        "3": "udp",
        "4": "icmp"
    }

    if choice not in filters:
        print("Invalid choice. Please select 1-4.")
        return

    selected_filter = filters[choice]

    # Create a fresh CSV file for this capture session
    with open(log_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Packet Number",
            "Timestamp",
            "Source IP",
            "Destination IP",
            "Protocol",
            "Source Port",
            "Destination Port",
            "Packet Length"
        ])

    print("\nStarting packet capture...")
    print("Selected filter:", selected_filter or "All IP protocols")
    print("Press Ctrl+C to stop capturing.")

    try:
        sniff(
            filter=selected_filter,
            prn=analyze_packet,
            store=False
        )

    except KeyboardInterrupt:
        print("\nSniffer stopped.")

    except Exception as error:
        print("\nCapture error:", error)

    finally:
        print("\nCAPTURE SUMMARY")
        print("=" * 35)
        print("Total packets analyzed:", packet_count)
        print("Saved packet details to:", log_file)


if __name__ == "__main__":
    start_sniffer()
