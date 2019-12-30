# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/11/18
'''
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor

__author__ = 'Fangyang'

# 耗cpu的操作, 在python中由于存在GIL锁, 多线程不是真正的多线程, 推荐用多进程
# 对于io操作, 瓶颈不在cpu, 推荐使用多线程编程
# 对于操作系统, 进程切换的代价要高于线程

# 1. 对于耗费cpu的操作, 计算, 多进程优于多线程
def fib(n):
    if n<=2:
        return 1
    return fib(n-1) + fib(n-2)

def random_sleep(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    # print(fib(10))

    # 1. 计算测试, 多进程优于多线程
    # start_time = time.time()
    # with ThreadPoolExecutor(3) as executor:   # 在windows下, 必须放在 if __name == "__main__": 下, linux没有这个问题
    #     all_task = [executor.submit(fib, (num)) for num in range(25, 40)]
    #     for future in as_completed(all_task):
    #         data = future.result()
    #         print("get {} page".format(data))
    # print('Thread cost : {:.2f}'.format(time.time() - start_time))
    #
    # start_time = time.time()
    # with ProcessPoolExecutor(3) as executor:   # 在windows下, 必须放在 if __name == "__main__": 下, linux没有这个问题
    #     all_task = [executor.submit(fib, (num)) for num in range(25, 40)]
    #     for future in as_completed(all_task):
    #         data = future.result()
    #         print("get {} page".format(data))
    # print('Process cost : {:.2f}'.format(time.time() - start_time))
    # # Thread cost: 110.00
    # # Process cost: 76.16

    # 2. io 操作测试, 多线程优于多进程
    start_time = time.time()
    with ThreadPoolExecutor(3) as executor:   # 在windows下, 必须放在 if __name == "__main__": 下, linux没有这个问题
        all_task = [executor.submit(random_sleep, (num)) for num in [2]*10]
        for future in as_completed(all_task):
            data = future.result()
            print("get {} page".format(data))
    print('Thread cost : {:.2f}'.format(time.time() - start_time))

    start_time = time.time()
    with ProcessPoolExecutor(3) as executor:   # 在windows下, 必须放在 if __name == "__main__": 下, linux没有这个问题
        all_task = [executor.submit(random_sleep, (num)) for num in [2]*10]
        for future in as_completed(all_task):
            data = future.result()
            print("get {} page".format(data))
    print('Process cost : {:.2f}'.format(time.time() - start_time))
    # Thread cost : 8.01
    # Process cost : 9.70
