# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/14
'''
__author__ = 'Fangyang'


def handle_item(item):
    return item**2


if __name__ == '__main__':

    #!!!! list生成式/推导式, 可以替代map, reduce, filter函数
    # list生成式性能高于列表操作
    odd_list = [i for i in range(21) if i%2 == 1]
    print(odd_list)

    odd_list2 = [handle_item(i) for i in range(10) if i%2 ==1]
    print(odd_list2)

    #!!!! 生成器表达式
    odd_gen = (i for i in range(21) if i%2 == 1)
    print(type(odd_gen))
    print(list(odd_gen))

    #!!!! 字典推导式
    my_dict = {'b1': 22, 'b2': 23, 'b3': 5}
    reversed_dict = {value: key for key, value in my_dict.items()}
    print(reversed_dict)

    # 集合set推导式, 这个可以加入自己的逻辑, 灵活性更高
    my_set = {key for key,value in my_dict.items()}
    print(type(my_set))
    print(my_set)