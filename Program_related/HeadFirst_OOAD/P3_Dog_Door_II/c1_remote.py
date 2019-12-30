# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/17
'''
__author__ = 'Fangyang'

from c1_dog_door import DogDoor


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

if __name__ == '__main__':
    print('dd')