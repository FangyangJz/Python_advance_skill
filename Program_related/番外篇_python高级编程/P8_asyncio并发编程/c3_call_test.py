# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/11/28
'''
__author__ = 'Fangyang'


import asyncio

def callback(sleep_time):
    print('sleep {} success'.format(sleep_time))

def stoploop(loop):
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.call_soon(callback, 2)
    loop.call_later(2, callback, 3)
    loop.call_later(3, callback, 3)
    # loop.call_soon(stoploop, loop)
    loop.run_forever()

