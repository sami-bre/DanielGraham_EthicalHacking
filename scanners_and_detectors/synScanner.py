from scapy.all import sr1
import sys

from scapy.layers.inet import IP, ICMP, TCP


def icmp_probe(ip):
    icmp_packet = IP(dst=ip) / ICMP()
    resp_packet = sr1(icmp_packet, timeout=10)
    return resp_packet is not None


def syn_scan(ip, port):

    syn_packet = IP(dst=ip) / TCP(dport=1800, flags='S')
    resp_packet = sr1(syn_packet, timeout=10)

    print("--------------")
    if resp_packet.getlayer('TCP').flags == 0x12:
        print("SYN ACK")
    elif resp_packet.getlayer('TCP').flags == 0x1:
        print('SYN')
    elif resp_packet.getlayer('TCP').flags == 0x02:
        print('ACK')
    else:
        print("something went wrong")
        print("the flag is {}".format(resp_packet.getlayer('TCP').flags))


if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    if icmp_probe(ip):
        syn_scan(ip, port)
    else:
        print("IP is down")
