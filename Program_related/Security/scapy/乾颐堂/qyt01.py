#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2019/8/14
'''
__author__ = 'Fangyang'

import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # 清楚报错
from scapy.all import *

localmac = 'd0:c6:37:d3:5f:ef'
localip = '192.168.1.159'

if __name__ == '__main__':
    print(localip)
