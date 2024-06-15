import pyshark

def capture_packets(interface, packet_count):
    capture = pyshark.LiveCapture(interface=interface)
    print(f"Capturing {packet_count} packets from interface {interface}...")

    # Sniff packets
    for packet in capture.sniff_continuously(packet_count=packet_count):
        # Print packet summary
        print(packet)

def main():
    interface = 'eth0'  # Replace with your network interface
    packet_count = 10   # Number of packets to capture

    capture_packets(interface, packet_count)

if __name__ == "__main__":
    main()
