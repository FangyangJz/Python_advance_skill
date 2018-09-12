# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/8/21
'''

__author__ = 'Fangyang'

# 1. 检查某个类是否有某种方法 hasattr(class, 'method')
class Company(object):
    def __init__(self, em):
        self.em = em

    def __len__(self):
        return len(self.em)


com = Company((1, 2, 3, 4))
print(hasattr(com, '__len__'))
print(len(com))

# 还有一种判断方法
from collections.abc import Sized
r = isinstance(com, Sized)
print(r)

