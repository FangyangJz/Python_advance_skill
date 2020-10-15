#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Datetime :   21/09/2020 01:28
@Author   :   Fangyang
"""
import sympy as sym
import matplotlib.pyplot as plt
import numpy as np


def numercial_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)


def tangent_line(f, x):
    a = numercial_diff(f, x)
    b = f(x) - a * x

    # def line(t):
    #     return a * t + b
    # return line

    return lambda t: a * t + b


if __name__ == "__main__":
    x = sym.symbols('x')
    expr = x ** 4
    r1 = sym.diff(expr, x, 1)
    r2 = sym.diff(expr, x, 2)
    r3 = sym.diff(expr, x, 3)

    print(r1, r2, r3)
    print(r3.evalf(subs={'x': 2}))

    x = np.arange(0, 20, 0.1)
    y = x ** 2
    plt.plot(x, y)

    # 求出切线方程
    t1 = tangent_line(lambda x: x ** 2, 10)
    y2 = t1(x)
    plt.plot(x, y2)

    plt.show()
