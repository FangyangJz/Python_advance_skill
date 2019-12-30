# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/15
'''
from datetime import date

__author__ = 'Fangyang'

# __getattr__ , 在查找不到属性的时候调用
# __getattibute__ , 无论访问 存在的 还是 不存在的 属性, 都调用这个, 把持了属性访问的入口
# 注意啊, __getattribute__ 尽量不要重写, 写不好容易崩溃

class User:
    def __init__(self, name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info = info

    # def __getattr__(self, item):
    #     print('找不到属性就调用我!')
    #     return '找不到属性就调用我!'

    def __getattr__(self, item):
        return self.info[item]


if __name__ == '__main__':

    user = User('b1', date(year=1987, month=1, day=1), info={'company': 'mmm'})
    # r = user.age
    # print(r)
    print(user.company)

