# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/15
'''
from datetime import date, datetime

__author__ = 'Fangyang'

class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    # def get_age(self):
    #     return datetime.now().year - self.birthday.year

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value


if __name__ == '__main__':
    user = User('b1', date(year=1987, month=1, day=1))
    # print(user.get_age())
    print(user.age)   # 可以用访问属性的方式来访问方法, 因为 @property
    user.age = 30
    print(user.age)
    print(user._age)  # 就是想说明 @propery 和 @funcname.setter 可以加入自定义逻辑
