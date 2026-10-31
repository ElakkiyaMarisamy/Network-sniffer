from scapy.all import sniff

packet = sniff(count=10)

packet.show()