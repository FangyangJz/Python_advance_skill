# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/10/7
'''
import time

__author__ = 'Fangyang'


# Semaphore 用于控制进入数量的锁
# 文件 写一般用于一个线程写, 读可以允许多个

import threading

class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print('got html text success')
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()   # 每次acquire一次, semaphore的参数减1, 减到0就不进入线程
            html_thread = HtmlSpider('https://www.dff/{}'.format(i), self.sem)
            html_thread.start()


if __name__ == '__main__':
    # Semaphore 控制某段代码进入线程的数量
    sem = threading.Semaphore(3)

    url_producer = UrlProducer(sem)
    url_producer.start()


