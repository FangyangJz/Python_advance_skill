# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/12/6
'''
__author__ = 'Fangyang'

def y():
    return [lambda x:x*i for i in range(3)]


print([m(1) for m in y()])






if __name__ == '__main__':
    pass


