# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/8/21
'''

__author__ = 'Fangyang'

# 鼓励用isinstance去判断类型

class A:
    pass

class B(A):
    pass

b = B()

print(isinstance(b, A))

print(type(b) is A)
print(type(b) is B)