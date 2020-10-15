#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Datetime :   22/09/2020 01:05
@Author   :   Fangyang
"""
from enum import Enum

import sympy as sym

if __name__ == "__main__":
    x, y = sym.symbols("x y")
    z1 = x ** 2 + y ** 2 - 4
    f = sym.idiff(z1, y, x)
    print(f)
    print(f.evalf(subs={'x': 2, 'y': 4}))

    z2 = 5 * sym.sin(x) + 3 * sym.sec(y) - y + x ** 2 - 3
    f2 = sym.idiff(z2, y, x)
    print(f2)
    print(f2.evalf(subs={'x': 0, 'y': 0}))
