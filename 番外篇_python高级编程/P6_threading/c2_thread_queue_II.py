# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/10/6
'''
__author__ = 'Fangyang'

# 线程间通信

import time
import threading
from queue import Queue

detail_url_list = []

def get_detail_html(queue):
    # 爬取文章详情页
    while True:
        if len(detail_url_list):
            url = queue.get()

            print('get detail html started')
            time.sleep(2)
            print('get detail html end')


def get_detail_url(queue):
    # 爬取文章列表页
    while True:
        print('get detail url started')
        time.sleep(4)
        for i in range(20):
            queue.put('http:// url/ {id}'.format(id=i))
        print('get detail url end')

# 2. 线程通信方式 之 queue, 进行线程间同步, 线程安全, 推荐

if __name__ == '__main__':

    detail_url_queue = Queue(maxsize=1000)

    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue))
    for i in range(10):  # 开10个爬取具体页面的线程
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue))
        html_thread.start()


