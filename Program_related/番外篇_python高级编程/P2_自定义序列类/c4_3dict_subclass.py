# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/14
'''
from collections import UserDict

__author__ = 'Fangyang'


class Mydict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value*2)


class Mydict2(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value*2)



if __name__ == '__main__':

    # 不建议继承list和dict
    # 因为用C语言写的方法, 不会调用我们override的方法
    my_dict = Mydict(one=1)
    print(my_dict)
    my_dict['one'] = 1
    print(my_dict)

    # 所以, 想继承dict, 推荐用collection模块的 UserDict, 这里面使用python写的
    my_dict2 = Mydict2(one=1)
    print(my_dict2)
    my_dict2['one'] = 1
    print(my_dict2)

    # collection 模块的 defaultdict (C语言写的) 其实是扩展了 __missing__
    # 可以指定默认值
