import scapy.all as scapy


def scan():
    arp_req = scapy.ARP(pdst="192.168.0.1/24")
    broadcast_req = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packet = broadcast_req/arp_req
    answered_list = scapy.srp(arp_packet, timeout=1, verbose=False )[0]

    print("[+] network scanning starting \n")
    for element in answered_list:
        print("ip > " + element[1].pdst + "\t mac > " + element[1].hwsrc )
    print("\n[+] Finished")


scan()
