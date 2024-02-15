import scapy.all as scapy
import optparse


def get_info():
    parse = optparse.OptionParser()
    parse.add_option("-t", "--target_ip", dest="target_ip", help="target ip")
    parse.add_option("-g", "--gateway", dest="gateway", help="gateway ip")
    res = parse.parse_args()[0]
    return res


def get_mac(ip):
    arp = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast/arp
    mac = scapy.srp(packet, timeout=1, verbose=False)[0][0][1].src
    print(mac)


get_mac("192.168.0.3")

res = get_info()
#print(res)
