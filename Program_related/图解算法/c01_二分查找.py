# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/12/31 上午1:16
# @Author   : Fangyang
# @Software : PyCharm


# 仅当列表是有序的时候才有用

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            print(f"Steps : {steps}")
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9, 11, 12, 13, 14, 15, 16, 20, 25]
    print(binary_search(my_list, 12))
    print(binary_search(my_list, 25))
