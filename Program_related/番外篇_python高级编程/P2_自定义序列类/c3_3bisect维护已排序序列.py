# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/14
'''
__author__ = 'Fangyang'

import bisect
# 处理已排序的序列, 用来维持已排序的序列, 升序
# 二分查找

# 1. 避免了先把数据收集齐再排序, 适用于变插数据, 边排序的情况
# 2. 二分查找, 效率高


if __name__ == '__main__':
    inter_list = []   #  list tuple deque 都行
    bisect.insort(inter_list, 3)
    bisect.insort(inter_list, 2)
    bisect.insort(inter_list, 5)
    bisect.insort(inter_list, 1)
    bisect.insort(inter_list, 6)
    print(inter_list)
    print(bisect.bisect_left(inter_list, 3))
    print(bisect.bisect_right(inter_list, 3))  # 默认是 bisect_right

    # 序列类型分类
    # 1. 容器序列 list tuple deque     # 可以在容器中放置任意不同类型的数据
    # 2. 扁平序列 str, bytes, bytearray, array.array  # 必须是相同类型的数据

    # 3. 可变序列 list deque, bytearray, array
    # 4. 不可变   str, tuple, bytes