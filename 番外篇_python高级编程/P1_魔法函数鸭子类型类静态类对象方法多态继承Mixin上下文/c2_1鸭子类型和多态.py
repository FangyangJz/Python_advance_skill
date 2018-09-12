# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/8/21
'''

__author__ = 'Fangyang'

# 我的理解鸭子类型是 都有一样的方法, 实现了不同的类, 给出不同的效果
# 所以 魔法函数 可以在不同的类中通用, 这不就是鸭子函数的思想么

class Cat(object):
    def say(self):
        print('i am a cat')

class Dog(object):
    def say(self):
        print('i am a dog')

class Duck(object):
    def say(self):
        print('i am a duck')


animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()


# 另一个例子, 用extend(self, iterable)展示的
# 函数的参数只要是可迭代类型就可以
a = [1,2,3]
a.extend(('a', 'b'))
print(a)