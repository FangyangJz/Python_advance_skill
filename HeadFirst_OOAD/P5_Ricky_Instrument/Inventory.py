# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/19
'''
__author__ = 'Fangyang'


from Instrument import Instrument, InstrumentSpec
from Guitar import GuitarSpec,Guitar
from Mandolin import MandolinSpec, Mandolin


class Inventory(object):

    def __init__(self, inventory_list=[]):
        self._inventory = inventory_list

    def addInstrument(self, serialNumber, price, spec):
        if isinstance(spec, GuitarSpec):
            instrument = Guitar(serialNumber, price, spec)
        elif isinstance(spec, MandolinSpec):
            instrument = Mandolin(serialNumber, price, spec)
        self._inventory.append(instrument)

    def getInstrument(self, serialNumber):
        for i in self._inventory:
            if i.getSerialNumber() == serialNumber:
                return i
        return None

    def search(self, guitar_spec):
        matchingGuitars = []
        for guitar in self.guitars:
            if guitar.getSpec().matches(guitar_spec):
                matchingGuitars.append(guitar)
        return matchingGuitars

if __name__ == '__main__':


