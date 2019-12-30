# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/19
'''
__author__ = 'Fangyang'


from Instrument import Instrument, InstrumentSpec
# from Guitar import GuitarSpec,Guitar
# from Mandolin import MandolinSpec, Mandolin


class Inventory(object):

    def __init__(self, inventory_list=[]):
        self._inventory = inventory_list

    def addInstrument(self, serialNumber, price, spec):
        # if isinstance(spec, GuitarSpec):
        #     instrument = Guitar(serialNumber, price, spec)
        # elif isinstance(spec, MandolinSpec):
        #     instrument = Mandolin(serialNumber, price, spec)
        instrument = Instrument(serialNumber, price, spec)
        self._inventory.append(instrument)

    def getInstrument(self, serialNumber):
        for i in self._inventory:
            if i.getSerialNumber() == serialNumber:
                return i
        return None

    def search(self, search_spec):
        matching_instruments = []
        for instrument in self._inventory:
            # if isinstance(search_spec, GuitarSpec) and instrument.getSpec().matches(search_spec):
            #     matching_instruments.append(instrument)
            # elif isinstance(search_spec, MandolinSpec) and instrument.getSpec().matches(search_spec):
            #     matching_instruments.append(instrument)

            if instrument.getSpec().matches(search_spec):  # 比对所有乐器
                matching_instruments.append(instrument)

        return matching_instruments

if __name__ == '__main__':
    pass


