import dpkt
import socket

def read_pcap_file(filename):
    with open(filename, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        for timestamp, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src_ip = socket.inet_ntoa(ip.src)
            dst_ip = socket.inet_ntoa(ip.dst)
            print(f"Source IP: {src_ip}, Destination IP: {dst_ip}")

def main():
    filename = 'example.pcap'   # Replace with your pcap file path

    read_pcap_file(filename)

if __name__ == "__main__":
    main()
