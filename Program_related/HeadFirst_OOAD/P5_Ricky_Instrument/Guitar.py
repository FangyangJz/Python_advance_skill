# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/18
'''
__author__ = 'Fangyang'

from Instrument import Instrument, InstrumentSpec

class Guitar(Instrument):
    def __init__(self, serialNumber, price, spec):
        super().__init__(serialNumber, price, spec)


class GuitarSpec(InstrumentSpec):

    def __init__(self, builder, model, types, backWood, topWood, numStrings=6):
        super().__init__(builder, model, types, backWood, topWood)
        self._numStrings = numStrings

    def getNumStrings(self):
        return self._numStrings

    def matches(self, otherSpec):
        if not isinstance(otherSpec, GuitarSpec):
            return False
        elif not super().matches(otherSpec):
            return False
        elif otherSpec.getNumStrings() != self.getNumStrings():
            return False
        return True


if __name__ == '__main__':
    pass


