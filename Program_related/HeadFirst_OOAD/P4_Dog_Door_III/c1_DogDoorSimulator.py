# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/17
'''
import time
import threading

__author__ = 'Fangyang'

import unittest
from c1_dog_door import DogDoor
from c1_remote import Remote
from c1_bark_recognizer import BarkRecognizer
from c1_bark import Bark

class DogDoorSimulator(unittest.TestCase):

    def setUp(self):
        print('test begin')
        self.dogdoor = DogDoor()
        self.dogdoor.addAllowedBark(Bark('rowlf'))
        self.dogdoor.addAllowedBark(Bark('rooooowlf'))
        self.dogdoor.addAllowedBark(Bark('rawlf'))
        self.dogdoor.addAllowedBark(Bark('woof'))

        self.remote = Remote(self.dogdoor)
        self.bark_recognizer = BarkRecognizer(self.dogdoor)

    def test_pressButton(self):
        print('------test pressButton')
        print('Door status is ' + str(self.dogdoor.isOpen()) + '. Fido bars to go outside')
        self.remote.pressButton()  # 开门
        self.assertTrue(self.dogdoor.isOpen(), 'Sorry, remote cannot open the door')
        print('Fido has gone outside')

        # 因为是异步定时器, 所以这里在按一下按钮, 关门.
        # 异步关门貌似 人工太快关的话, 会夹到狗狗啊....
        self.remote.pressButton()
        self.assertFalse(self.dogdoor.isOpen(), 'Sorry, remote cannot close the door')

    def test_pressButton_delay(self):
        print('------test pressButton delay')
        print('Door status is ' + str(self.dogdoor.isOpen()) + '. Fido bars to go outside')
        self.remote.pressButton()   # 开门, 测试5s自动关门功能
        self.assertTrue(self.dogdoor.isOpen(), 'Sorry, remote cannot open the door')
        time.sleep(5.5)
        self.assertFalse(self.dogdoor.isOpen(), 'Sorry, remote cannot close the door')

    def test_barkRecognizer(self):
        print('-----test_barkRecognizer')
        print('Door original status is ' + str(self.dogdoor.isOpen()) + ' Fido bars to go outside')
        print('------test bark allowed')
        self.bark_recognizer.recognize(Bark('rowlf'))
        self.assertTrue(self.dogdoor.isOpen(), 'Sorry, bark recognizer cannot open the door')

        # 测试后将门关闭, 要不计时器线程会对后面门的状态产生影响
        print('set the door to closed, avoid to effect the following test case results')
        self.dogdoor.close()

        # 其他狗狗的叫声
        print('------test not allowed bark')
        print('Door original status is ' + str(self.dogdoor.isOpen()) + ' Fido bars to go outside')
        self.bark_recognizer.recognize(Bark('yyyyyyyyyyy'))
        self.assertFalse(self.dogdoor.isOpen(), 'Nooo, bark recognizer open the door for not allowed')
        print('set the door to closed, avoid to effect the following test case results')
        self.dogdoor.close()

    def tearDown(self):
        print('test over')
        print('')
        self.dogdoor = None
        self.remote = None


if __name__ == '__main__':
    unittest.main()
