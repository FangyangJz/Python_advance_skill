#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Datetime :   02/10/2020 23:34
@Author   :   Fangyang
"""

import sympy as sym

x = sym.Symbol('x')
func1 = sym.E ** 2 + 2 * x
result = sym.integrate(func1, x)
print(result)

result1 = sym.integrate(func1, (x, 0, 1))  # 对x求积分, 下限0, 上限1
print(result1)

func2 = (x ** 2) * sym.cos(x ** 3)
result2 = sym.integrate(func2, x)
print(result2)

if __name__ == "__main__":
    pass
