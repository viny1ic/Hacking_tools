from scapy.all import Ether, ARP, srp, conf

def arp_scan(iface, ip):
    print("[+] Scan started")
    conf.verb = 0
    broadcast = "ff:ff:ff:ff:ff:ff"
    ether_layer= Ether(dst=broadcast)
    arp_layer=ARP(pdst=ip)
    packet= ether_layer/arp_layer
    ans, unans= srp(packet, iface=iface, timeout=5, inter=0.1)
    for sent, recieved in ans:
        recieved_ip=recieved[ARP].psrc
        recieved_mac=recieved[Ether].src
        print("IP= ", recieved_ip,"MAC= ", recieved_mac, "Discovered")
    print("[+] Scan completed")
# if __name__=="__main__":
print("[+] Run script with sudo if it doesnt work")

iface=input("enter name of interface: ")
ip=input("enter IP address/range")
arp_scan(iface, ip)