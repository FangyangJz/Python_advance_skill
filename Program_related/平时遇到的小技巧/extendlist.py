# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/12/6
'''
__author__ = 'Fangyang'


def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')



if __name__ == '__main__':
    print("list1 = %s " % list1)
    print("list2 = %s " % list2)
    print("list3 = %s " % list3)

