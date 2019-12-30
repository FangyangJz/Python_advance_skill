# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/11/26
'''
__author__ = 'Fangyang'

import types

# python为了将语义变得明确, 就引入了async和await关键词用于定义原生的协程
# async def downloader(url):
#     return 'fangyang'

@types.coroutine
def downloader(url):
    yield 'fangyang'

async def download_url(url):
    html = await downloader(url)
    # async 里面只能出现 await, 不能出现yield
    # 正常函数里面同样不能出现 await
    # await的函数里面也不能出现yield, 想出现, 需要加 @types.coroutine
    # await 我们可以理解成 yield from
    return html


if __name__ == '__main__':
    coro = download_url('http://www.baidu.com')
    # next(None)   # 使用原生协程调用的时候不能使用这种方式
    coro.send(None)


