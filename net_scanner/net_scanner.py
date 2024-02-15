import scapy.all as scapy


def scan():
    arp_req = scapy.ARP(pdst="192.168.0.1/24")
    broadcast_req = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packet = broadcast_req/arp_req
    answered_list = scapy.srp(arp_packet, timeout=2, verbose=False)[0]

    client_list = []
    for element in answered_list:
        clients_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(clients_info)

    for element in client_list:
        print(element)


scan()
