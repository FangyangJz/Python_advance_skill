# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2019/12/5 15:20
# @Author  : Fangyang
# @Software: PyCharm

import time


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def testFib(n):
    for i in range(n + 1):
        print('fib of', i, '=', fib(i))


start_time = time.time()
print(testFib(38), f'time cost {time.time() - start_time:.2f}s')

if __name__ == '__main__':
    pass
