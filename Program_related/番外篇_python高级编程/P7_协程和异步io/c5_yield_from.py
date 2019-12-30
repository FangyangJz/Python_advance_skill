# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/11/19
'''
__author__ = 'Fangyang'

from itertools import chain


my_list = [1,2,3]
my_dict = {
    'b1': 'dddddddd',
    'b2': '2222222222'
}

def my_chain(*args, **kwargs):
    for my_iterable in args:
        for value in my_iterable:
            yield value

def my_chain2(*args, **kwargs):
    for my_iterable in args:
        yield from my_iterable


for value in chain(my_list, my_dict, range(5,10)):
    print(value)

print('-'*50)
for value in my_chain(my_list, my_dict, range(5,10)):
    print(value)

print('='*50)
for value in my_chain2(my_list, my_dict, range(5,10)):
    print(value)

#############################################
def g1(iterable):
    yield range(10)

def g2(iterable):
    yield from range(10)

#############################################
# 1. main 调用方, gg1 委托生成器, gen 子生成器
# 2. yield from 会在调用方与子生成器之间建立一个 双向 通道
def gg1(gen):
    yield from gen

def main():
    g = gg1()
    g.send(None)


if __name__ == '__main__':
    for value in g1(range(10)):
        print(value)

    for value in g2(range(10)):
        print(value)


