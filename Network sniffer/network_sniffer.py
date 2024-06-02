from scapy.all import sniff
from scapy.layers.inet import IP


def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"IP Packet: {ip_src} -> {ip_dst}")


def main():
    print("Starting network sniffer...")
    sniff(prn=packet_callback, store=0)


if __name__ == "__main__":

    main()


