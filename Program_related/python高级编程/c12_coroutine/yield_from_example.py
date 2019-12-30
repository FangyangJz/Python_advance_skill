# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2019/8/11
'''
__author__ = 'Fangyang'

final_result = {}


def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield
        print(pro_name + "销量:", x)
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums


def middle(key):
    while True:
        final_result[key] = yield from sales_sum(key)
        print(key + "销量统计完成!")


def main():
    data_sets = {
        "ff": [1200, 1599, 1322],
        "dd": [28, 12, 22, 33],
        "cc": [11, 2, 3, 4]
    }

    for key, data_set in data_sets.items():
        print("start key:", key)
        m = middle(key)
        m.send(None)
        for value in data_set:
            m.send(value)
        m.send(None)
    print("final_result:", final_result)

if __name__ == '__main__':
    main()
