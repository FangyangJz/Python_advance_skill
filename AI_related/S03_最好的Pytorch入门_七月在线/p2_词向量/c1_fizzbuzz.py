# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/12/8 下午5:09
# @Author   : Fangyang
# @Software : PyCharm


def fizz_buzz_encode(i):
    if i % 15 == 0:
        return 3
    elif i % 5 == 0:
        return 2
    elif i % 3 == 0:
        return 1
    else:
        return 0


def fizz_buzz_decode(i, prediction):
    return [str(i), 'fizz', 'buzz', 'fizzbuzz'][prediction]


def helper(i):
    print(fizz_buzz_decode(i, fizz_buzz_encode(i)))


for i in range(16):
    helper(i)

if __name__ == '__main__':
    pass
