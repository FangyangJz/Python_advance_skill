# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/11/19
'''
__author__ = 'Fangyang'

final_result = {}

def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield
        print(pro_name + '销量: ', x)
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums

def middle(key):
    while True:
        final_result[key] = yield from sales_sum(key)
        print(key+'销量统计完成!!')

def main():
    data_sets = {
        '面膜': [1200, 1500, 3000],
        '收集': [28, 55, 98, 108],
        '大衣': [220, 442, 331, 23],
    }
    for key, data_sets in data_sets.items():
        print('start key: ', key)
        m = middle(key)
        m.send(None)  # 预激middle协程
        for value in data_sets:
            m.send(value)
        m.send(None)
    print('final_result: ', final_result)


if __name__ == '__main__':
    main()


