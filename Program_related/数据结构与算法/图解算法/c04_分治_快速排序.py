# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2020/1/1 下午11:32
# @Author   : Fangyang
# @Software : PyCharm


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    print(quick_sort([5, 2, 22, 3, 1, 6, 5, 12, 9, 10]))
