# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/14
'''
__author__ = 'Fangyang'

from collections.abc import Mapping, MutableMapping   # MutableMapping 就是 dict


if __name__ == '__main__':

    a = {}
    print(isinstance(a, MutableMapping))
