#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Datetime :   19/09/2020 21:10
@Author   :   Fangyang
"""

import sympy as sym

def numercial_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)


def func_1(x):
    return x ** 2


if __name__ == "__main__":
    diff = numercial_diff(func_1, 5)
    print(diff)

    x = sym.symbols('x')
    expr = x**2
    d = sym.diff(expr)
    print(d)
    print(d.evalf(subs={"x": 5}))  # 比自己手写的更精确
