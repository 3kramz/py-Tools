import subprocess
import optparse
import re


def get_input():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Input interface name")
    parser.add_option("-m", "--mac", dest="mac", help="Add new mac address")
    (options, arg) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.mac:
        parser.error("[-] Please specify new mac address, use --help for more info.")
    return options


def mac_changer(interface, mac):
    ifconfig = "ifconfig"
    print("[+] Changing mac...")
    subprocess.call([ifconfig, interface, "down"])
    subprocess.call([ifconfig, interface, "hw", "ether", mac])
    subprocess.call([ifconfig, interface, "up"])


def check_mac(iface, mac):
    ifconfig = subprocess.check_output(["ifconfig", iface])
    mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    if mac_search_result.group(0) == mac:
        print("[+] Mac address change to " + mac + " Successfully")
    else:
        print("[-] Failed to change mac address")


options = get_input()
mac_changer(options.interface, options.mac)
options = get_input()
check_mac(options.interface, options.mac)
