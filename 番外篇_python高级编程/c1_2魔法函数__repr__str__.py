# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/8/21
'''

__author__ = 'Fangyang'


class Company0(object):
    def __init__(self, employee_list):
        self.employee = employee_list

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __repr__(self):
        '''这个应该是ipython中显示的'''
        return '我是repr'

    def __str__(self):
        return '我是str'

c0 = Company0([1, 2])
c = Company([1, 2, 3, 4])
print(c0)
print(c)

