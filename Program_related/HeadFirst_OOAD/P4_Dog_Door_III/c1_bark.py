# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/18
'''
__author__ = 'Fangyang'

class Bark(object):

    def __init__(self, sound):
        self.sound = sound

    def getSound(self):
        return self.sound

    def equals(self, bark):
        if isinstance(bark, Bark):
            if self.sound == bark.sound:
                return True
        return False


# if __name__ == '__main__':
