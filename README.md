# codealpha_basic_network_sniffer
This is the task 1  of  Cybersecurity,Creating a Network Sniffer.

The project is a network sniffer built with Python, utilizing the scapy library to capture and analyze network traffic. It monitors packets in real-time and logs the source and destination IP addresses.

The key components of the project include the 'scapy' library, which is used for handling network packets in Python. The packet callback function, 'packet_callback(packet)', processes each packet, checks for IP information, and prints the source and destination addresses.

 The main function initializes the sniffer and uses the 'sniff()' function to capture packets in real-time, utilizing the callback function to process them.
