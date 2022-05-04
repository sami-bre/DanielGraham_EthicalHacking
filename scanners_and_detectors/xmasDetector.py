import sys

from scapy.all import sniff


def process_packet(pac):
    if pac['IP'].dst == '192.168.1.100' and pac.getlayer('TCP').flags == 'PFU':
        print("xmas detected from {}".format(pac['IP'].src))


if __name__ == '__main__':
    print('Listening for xmas scan on this machine')
    try:
        sniff(filter='tcp', count=0, prn=process_packet)
    except KeyboardInterrupt:
        sys.exit()
