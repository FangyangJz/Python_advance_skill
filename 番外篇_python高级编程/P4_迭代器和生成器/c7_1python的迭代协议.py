# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/16
'''
__author__ = 'Fangyang'
# 迭代器是访问集合内元素的一种方式, 一般用来遍历数据
# 迭代器和用下标访问的方式不同, 迭代器是不能返回的, 迭代器提供了一种惰性访问数据的方式
# 迭代协议  __iter__, __next__

from collections.abc import Iterable, Iterator

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee) # 这里要返回迭代器, 返回int会报错

    def __getitem__(self, item):   # 实现下标索引和切片
        return self.employee[item]

# 我们设计的迭代器功能的类的时候, 不要在类里面加 __next__,
# 正确的做法是独立写个迭代器类, 然后在 上面 __iter__中实例化迭代器类, 实现迭代器功能
# 如果__next__写在类里面, 还得维护一个self.index, 不符合设计原则
# 就像这里上下文写的这样

class MyIterator(Iterator):

    # def __iter__(self):  # 如果没有继承Iterator, 就需要这个
    #     return self

    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0   # 迭代器里面要维护这个index

    def __next__(self):  # 继承Iterator, 自定义__next__, 实现next()
        try:     # 因为index可能会超出list范围, 这里可能会抛出异常, 所有用try
            word = self.iter_list[self.index] # 真正返回迭代值的逻辑
        except IndexError:
            raise StopIteration

        self.index += 1
        return word


if __name__ == '__main__':

    # a = [1, 2]
    # print(isinstance(a, Iterable))
    # print(isinstance(a, Iterator))
    #
    # iter_ator = iter(a)  # 把Iterable变成Iterator
    # print(isinstance(iter_ator, Iterator))
    #
    company = Company(['tom', 'bob', 'jane'])
    # print(company[1:])

    # my_itor = iter(company)
    # while True:
    #     try:
    #         print(next(my_itor))
    #     except StopIteration:
    #         pass

    # 对于迭代器, for语句里面有StopIteration, 就不用像上面写的那么麻烦了
    for item in company:
        # for循环这里隐含着调用iter(company), 先去类里面找__iter__,
        # 找不到就去调用__getitem__(self, item), item从0开始
        # 如果__getitem__也没有, 就会抛出异常
        print(item)
