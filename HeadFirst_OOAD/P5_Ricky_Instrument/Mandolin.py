# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/18
'''
__author__ = 'Fangyang'

from Instrument import Instrument, InstrumentSpec


class Mandolin(Instrument):
    def __init__(self):
        super().__init__(serialNumber, price, spec)


class MandolinSpec(InstrumentSpec):
    def __init__(self, style):
        super().__init__(builder, model, types, backWood, topWood)
        self._style = style

    def getStyle(self):
        return self._style

    def matches(self, otherSpec: MandolinSpec):
        if not isinstance(otherSpec, MandolinSpec):
            return False
        elif not super().matches(otherSpec):
            return False
        elif otherSpec.getStyle() != self.getStyle():
            return False
        return True

if __name__ == '__main__':


