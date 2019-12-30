# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2019/8/11
'''
__author__ = 'Fangyang'

# python3.3 新加的 yield from
from itertools import chain

my_list = [1, 2, 3]
my_dict = {
    "f1": "baidu",
    "f2": "sina"
}

for value in chain(my_list, my_dict, range(5,10)):
    print(value)

print("-0-"*50)

def my_chain(*args, **kwargs):
    for my_iterable in args:
        for value in my_iterable:
            yield value

for value in my_chain(my_list, my_dict, range(5,10)):
    print(value)

print("=0-"*50)

def my_chain(*args, **kwargs):
    for my_iterable in args:
        yield from my_iterable
        # for value in my_iterable:
        #     yield value

for value in my_chain(my_list, my_dict, range(5,10)):
    print(value)

##################################################
def g1(gen):
    yield from gen

def main():
    g = g1(range(10))
    g.send(None)
    # 1. main 调用方 g1(委托生成器) gen 子生成器
    # 2. yield from 会在调用方与子生成器之间建立一个双向通道

if __name__ == '__main__':
    main()
