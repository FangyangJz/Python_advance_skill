# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/17
'''
import time
import threading

__author__ = 'Fangyang'

import unittest
from c1_dog_door import Remote, DogDoor

class DogDoorSimulator(unittest.TestCase):

    def setUp(self):
        self.dogdoor = DogDoor()
        self.remote = Remote(self.dogdoor)

    def test_pressButton(self):
        print('Door original status is False. Fido bars to go outside')
        self.remote.pressButton()   # 开门
        self.assertTrue(self.dogdoor.isOpen(), 'Sorry, remote cannot open the door')
        print('Fido has gone outside')

        # 因为是异步定时器, 所以这里在按一下按钮, 关门.
        # 异步关门貌似 人工太快关的话, 会夹到狗狗啊....
        self.remote.pressButton()
        self.assertFalse(self.dogdoor.isOpen(), 'Sorry, remote cannot close the door')

    def test_pressButton_delay(self):
        self.remote.pressButton()   # 开门, 测试5s自动关门功能
        self.assertTrue(self.dogdoor.isOpen(), 'Sorry, remote cannot open the door')
        time.sleep(5.5)
        self.assertFalse(self.dogdoor.isOpen(), 'Sorry, remote cannot close the door')

    def tearDown(self):
        self.dogdoor = None
        self.remote = None

if __name__ == '__main__':
    unittest.main()

