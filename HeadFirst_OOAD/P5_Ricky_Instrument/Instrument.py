# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/18
'''
__author__ = 'Fangyang'

class Instrument(object):
    def __init__(self, serialNumber, price, spec):
        self._serialNumber = serialNumber
        self._price = price
        self._spec = spec

    def getSerialNumber(self):
        return self._serialNumber

    def getPrice(self):
        return self._price

    def setPrice(self, new_price):
        self._price = new_price

    def getSpec(self):
        return self._spec


class InstrumentSpec(object):
    def __init__(self, properties_dict=None):
        self.properties = properties_dict
        # hashable(生命周期里不可变, 字典整体是可哈希的, 里面随便),
        # MutableMapping(字典里面是可以随便变化的)

    def getProperties(self):
        return self.properties

    def getProperty(self, strings):
        return self.properties.get(strings)

    def matches(self, otherSpec):
        # 试了下 两个字典如果键值都相等, 那么就返回true
        if otherSpec.getProperties() == self.getProperties():
            return True
        return False


if __name__ == '__main__':
    pass


