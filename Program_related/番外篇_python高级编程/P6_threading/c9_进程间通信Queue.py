# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/11/18
'''
import time

__author__ = 'Fangyang'

from multiprocessing import Process, Queue, Pool  # 注意,这个Queue不能用于 Pool 进程池
from multiprocessing import Manager  # 那么进程间怎么通信? 用这个Manager
# from queue import Queue  # 这个Queue只能用于多线程, 不能用于多进程


def producer(queue):
    queue.put('a')
    time.sleep(2)

def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)


if __name__ == '__main__':
    # queue = Queue(10)
    # my_producer = Process(target=producer, args=(queue, ))
    # my_consumer = Process(target=consumer, args=(queue, ))
    # my_producer.start()
    # my_consumer.start()
    # my_consumer.join()
    # my_producer.join()


    # queue = Queue(10)  # Multiprocessing 中的Queue无法用在pool中
    queue = Manager().Queue(10)  # 用这个Manager中的Queue
    pool = Pool(2)
    pool.apply_async(producer, args=(queue, ))
    pool.apply_async(consumer, args=(queue, ))
    pool.close()
    pool.join()