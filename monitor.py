#! /usr/bin/env python
from scapy.all import *

def monitor_callback(pkt):
    if not pkt.haslayer(Dot11): # Discard frames with no 802.11 headers
        return
    if pkt.type == 1: # Discard control frames
        return
    print pkt.time, pkt[Dot11].addr2

sniff(iface='wlan0',prn=monitor_callback, store=0)
