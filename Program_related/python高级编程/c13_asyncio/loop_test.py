# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2019/8/11
'''
__author__ = 'Fangyang'
# 事件循环 + 回调(驱动生成器) + epoll(IO多路复用)

import asyncio
import time


async def get_html(url):
    print("start get url")
    # time.sleep(5)  # 这种同步阻塞io是不能使用在 async 中的
    await asyncio.sleep(2)  # 注意这种要用await等待
    print("end get url")


if __name__ == '__main__':
    # start_time = time.time()
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(get_html("baidu"))
    # print("loop cost : {:.2f}s".format(time.time()-start_time))

    start_time = time.time()
    loop = asyncio.get_event_loop()
    task = [get_html("baidu_{}".format(i)) for i in range(10)]
    loop.run_until_complete(asyncio.wait(task))
    print("loop cost : {:.2f}s".format(time.time()-start_time))
