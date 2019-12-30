# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/11/19
'''
__author__ = 'Fangyang'


def gen_func():
    try:
        yield 'ddddddd'
    # print(html)
    except GeneratorExit:
        raise StopIteration
    # yield 2  # 注释掉这两行yield, close 就不会抛出 GeneratorExit 异常
    # yield 3
    return 'fangyang'


if __name__ == '__main__':
    gen = gen_func()
    next(gen)
    gen.close()
    next(gen)


