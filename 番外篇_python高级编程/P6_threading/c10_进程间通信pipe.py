# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/11/18
'''
__author__ = 'Fangyang'

from multiprocessing import Pipe, Pool, Process

def producer(pipe):
    pipe.send('boddy')

def consumer(pipe):
    print(pipe.recv())

# pipe 的性能高于 Queue, 因为Queue加了很多lock


if __name__ == '__main__':
    # 和Queue不同, Pipe只能适用于2个进程间通信
    receive_pipe, send_pipe = Pipe()
    my_producer = Process(target=producer, args=(send_pipe, ))
    my_consumer = Process(target=consumer, args=(receive_pipe, ))

    my_producer.start()
    my_consumer.start()

    my_producer.join()
    my_consumer.join()

