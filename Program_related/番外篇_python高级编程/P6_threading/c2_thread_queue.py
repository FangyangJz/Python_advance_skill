# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/10/6
'''
__author__ = 'Fangyang'

# 线程间通信

import time
import threading


detail_url_list = []

def get_detail_html(detail_url_list):
    # 爬取文章详情页
    # global detail_url_list  # 这里用参数传递, 所以不需要全局变量

    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()  # 从队列中弹出一个再去操作

            # for url in detail_url_list:
            #     print('get detail html started')
            #     time.sleep(2)
            #     print('get detail html end')

            print('get detail html started')
            time.sleep(2)
            print('get detail html end')


def get_detail_url(url):
    # 爬取文章列表页
    while True:
        print('get detail url started')
        time.sleep(4)
        for i in range(20):
            detail_url_list.append('http:// url/ {id}'.format(id=i))
        print('get detail url end')

# 1. 线程通信方式 之 共享变量, 不推荐, 线程不安全, 需要线程锁来保证安全

if __name__ == '__main__':
    thread_detail_url = threading.Thread(target=get_detail_url, args=(url))
    for i in range(10):  # 开10个爬取具体页面的线程
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_list))
        html_thread.start()


