# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2019/8/11
'''
__author__ = 'Fangyang'


def gen_func():
    try:
        yield "www.baidu.com"
    except Exception:
        # print("eeeeeeee")
        # raise StopIteration
        pass
    yield 2
    yield 3
    yield 4
    yield 5
    return "fangyang"


if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    # 下面这句throw 越过了 yeild 2, 异常类型必须是前后一致, 这里是Exception
    gen.throw(Exception, "ddddddddddddddddd")
    print(next(gen))
    gen.throw(Exception, "ddddddddddddddddd")
