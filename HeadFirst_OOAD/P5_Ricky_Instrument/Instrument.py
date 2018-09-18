# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/18
'''
__author__ = 'Fangyang'

class Instrument(object):
    def __init__(self, serialNumber, price, spec: InstrumentSpec):
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
    def __init__(self, builder, model, types, backWood, topWood):
        self._builder = builder
        self._model = model
        self._types = types
        self._backWood = backWood
        self._topWood = topWood

    def getBuilder(self):
        return self._builder

    def getModel(self):
        return self._model

    def getTypes(self):
        return self._types

    def getBackWood(self):
        return self._backWood

    def getTopWood(self):
        return self._topWood

    def matches(self, otherSpec):
        if self._builder != otherSpec.getBuilder():
            return False

        if self._model is not None:
            pass

        if self._types != otherSpec.getTypes():
            return False

        if self._backWood != otherSpec.getBackWood():
            return False

        if self._topWood != otherSpec.getTopWood():
            return False

        return True
_
if __name__ == '__main__':


