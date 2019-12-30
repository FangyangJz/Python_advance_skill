# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2019/8/11
'''
__author__ = 'Fangyang'


def gen_func():
    try:
        html = yield "www.baidu.com"
        print(html)
    except GeneratorExit:
        print("eeeeeeee")
        raise StopIteration
    yield 2
    yield 3
    return "fangyang"


if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    gen.close()
    print(next(gen))
