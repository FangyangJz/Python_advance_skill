# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/11/27
'''
__author__ = 'Fangyang'

# 事件循环 + 回调(驱动生成器) + epoll (IO多路复用)
# asyncio 是python用于解决异步io编程的一整套解决方案

import asyncio
import time
from functools import partial  # 对原有函数尽兴包装扩充

async def get_html(url):
    print('start get url')
    # time.sleep(2) # 这个是在同步阻塞中使用的, 这里不能使用
    await asyncio.sleep(2)  # 要这么sleep
    print('end get url')
    return 'fangyang'

def callback(url, future):  # 利用partial 增加一个url参数, 这个参数必须放在前面
    print(url)
    print("send email to boddy")



if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # get_future = asyncio.ensure_future(get_html('www.hjhh.com'))
    # tasks = [get_html('www') for i in range(10)]
    task = loop.create_task(get_html('sss.ddd.com'))
    task.add_done_callback(partial(callback, 'new extension url'))  # 原来这里只能有一个callback, 一个参数, 这里用partial尽兴参数扩充
    # loop.run_until_complete(asyncio.gather(*tasks))
    loop.run_until_complete(task)
    # loop.run_until_complete(get_future)
    print(time.time() - start_time)

    print(task.result())  # task 是future的一个子类
    # print(get_future.result())
