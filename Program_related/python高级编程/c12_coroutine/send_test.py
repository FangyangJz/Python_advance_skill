# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2019/8/11
'''
__author__ = 'Fangyang'


def gen_func():
    html = yield "http://www.baidu.com"
    print(html)
    yield 2
    yield 3
    return "fangyang"


if __name__ == '__main__':
    gen = gen_func()
    url = next(gen)
    html = "ff"
    # 在调用send发送非none值之前, 必须启动一次生成器, 这里用next做第一次启动(或者send(None)启动)
    print(gen.send(html))  # send不但传值还next
