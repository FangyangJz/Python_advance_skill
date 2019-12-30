# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/11/18
'''
__author__ = 'Fangyang'


# epoll并不代表一定比select好
#     在并发高的情况下, 连接活跃度不是很高, epoll比select好
#     并发性不高, 连接很活跃, select比epoll好


# 通过非阻塞io实现http请求
from selectors import DefaultSelector  # 会根据平台自己选择select(windows)还是epoll(linux)
from selectors import EVENT_READ, EVENT_WRITE
import socket
from urllib.parse import urlparse


selector = DefaultSelector()  # windows下需要加参数, linux不加参数默认使用epoll
urls = ['https://www.baidu.com']  # windows下改进
stop = False


class Fethcher(object):

    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode('utf-8'))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        data = b''
        d = self.client.recv(1024)
        if d:
            print(d)
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode('utf8')
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b''
        if self.path == "":
            self.path = '/'

        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)

        try:
            self.client.connect((self.host, 80))  # 阻塞不会消耗cpu
        except BlockingIOError as e:
            pass

        # 注册
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


def loop():
    # 事件循环, 不停的请求socket的状态并调用对应的回调函数
    # 1. select 本身不支持register模式
    # 2. socket状态变化以后的回调是由程序员完成的
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)

    # 回调 + 事件循环 + select(poll / epoll)


if __name__ == '__main__':
    fetcher = Fethcher()
    fetcher.get_url("https://www.baidu.com")
    loop()

    # 这个例子的代码存在 回调之痛
    # 1. 可读性差
    # 2. 共享状态管理困难
    # 3. 异常处理困难
    # 解决办法, 协程

