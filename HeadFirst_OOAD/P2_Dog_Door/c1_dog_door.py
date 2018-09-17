# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/17
'''
import threading
# import time

__author__ = 'Fangyang'


class DogDoor(object):

    def __init__(self):
        self.status = False
        self.timer = None
        self.delay_close_time = 5

    def open(self):
        print("The dog door opens.")
        self.status = True
        self.timer = threading.Timer(self.delay_close_time, self.close)
        self.timer.start()

    def close(self):
        if self.status is True:
            print("The dog door closes.")
            self.status = False
            self.timer.cancel()
        else:
            print('The door is closed. Do nothing!')

    def isOpen(self):
        return self.status


class Remote(object):

    def __init__(self, door: DogDoor):
        self.door = door

    def pressButton(self):
        print("Pressing the remote control button...")
        if self.door.isOpen():
            self.door.close()
        else:
            self.door.open()
            # 定时器应该是门的特性, 不是remote的
            # 这里开启一个线程跑定时器, 是异步的方式,
            # 也可以用time.sleep(5) 同步阻塞的方式, 想了一下, 同步的话,可以把逻辑放在remote里
            # timer = threading.Timer(5, self.door.close)  # 5s后执行关门
            # timer.start()   # 启动定时器


def fun_timer():
    print('Hello Timer!')
    # global timer
    timer = threading.Timer(5, fun_timer)
    timer.start()
    timer.cancel()  # 5s在另一个thread中执行, cancel在本线程,马上执行会删了另一个线程

# if __name__ == '__main__':

    # timer = threading.Timer(1, fun_timer)
    # timer.start()

    # time.sleep(2) # 15秒后停止定时器
    # timer.cancel() # 调用cancel, 及时回收垃圾

    # dogdoor = DogDoor()
    # remote = Remote(dogdoor)
    # print(dogdoor.status)
    # remote.pressButton()
    # print(dogdoor.status)
    # time.sleep(6)
    # print(dogdoor.status)