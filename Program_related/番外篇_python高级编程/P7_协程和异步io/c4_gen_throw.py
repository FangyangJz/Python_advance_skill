# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/11/19
'''
__author__ = 'Fangyang'


def gen_func():

    try:
        yield 'ddddddd'
    except Exception as e:
        pass
    yield 2
    yield 3
    return 'fangyang'


if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    gen.throw(Exception, "download error")
    print(next(gen))
    gen.throw(Exception, 'download error')

