#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Datetime :   19/09/2020 13:33
@Author   :   Fangyang
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym


if __name__ == "__main__":
    x = sym.Symbol('x')
    f1 = sym.sin(x)/x
    L = sym.limit(f1, x, "oo")
    print(f"{f1} 的趋于 oo 的极限是{L}")
    L = sym.limit(f1, x, 0)
    print(f"{f1} 的趋于 oo 的极限是{L}")

    x1 = np.arange(-100, 100, 0.01)
    y1 = np.sin(x1)/x1
    plt.figure(figsize=(12,5))
    plt.title("y = sin(x)/x")
    plt.plot(x1, y1)
    plt.show()