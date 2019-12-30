# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/10/7
'''
import dis
import threading

__author__ = 'Fangyang'

total = 0
lock = threading.Lock()
# 用锁会有两个问题:
# 1. 影响性能, 速度变慢
# 2. 锁会引起死锁

# RLock允许在同一个线程里,可以连续调用多次acquire, 注意acquire的次数要和release相等
rlock = threading.RLock()

def add():
    global total
    global lock  # 增加锁机制
    for i in range(1000000):
        lock.acquire()   # 获取锁
        total += 1
        lock.release()   # 释放锁

def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()

def add1(a):
    a += 1

def desc1(a):
    a -= 1



if __name__ == '__main__':
    thread1 = threading.Thread(target=add)
    thread2 = threading.Thread(target=desc)
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print(total)  # 增加了lock后, 结果为0

    # print(dis.dis(add1))
    # print(dis.dis(desc1))

# 0 LOAD_FAST                0 (a)   # 这里load完释放可能切到另一个线程对a做修改, 导致store的并不是想要的结果
# 2 LOAD_CONST               1 (1)
# 4 INPLACE_ADD
# 6 STORE_FAST               0 (a)
# 防止上面问题的出现, Python中的threading模块提供了 Lock
