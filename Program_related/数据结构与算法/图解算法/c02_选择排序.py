# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2020/1/1 下午3:07
# @Author   : Fangyang
# @Software : PyCharm


def findSmallestIndex(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallestIndex(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr


if __name__ == "__main__":
    arr = [4, 5, 1, 2, 3, 7, 8, 12, 1, 0, 20, -10, -26]
    print(arr)
    arr_sorted = selectionSort(arr)
    print(arr_sorted)
