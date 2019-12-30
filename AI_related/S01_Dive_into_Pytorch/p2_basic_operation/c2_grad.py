# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/12/23 上午12:33
# @Author   : Fangyang
# @Software : PyCharm


import torch

x = torch.ones(2, 2, requires_grad=True)
print(x, x.grad_fn)
y = x + 2
print(y, y.grad_fn)
print(x.is_leaf, y.is_leaf)

z = y * y * 3
out = z.mean()
print(z, out)
out.backward()
print(f"(d(out)/dx | x=1) = {x.grad}")

# 可以通过 .requires_grad_() 来用in-place的方式改变requires_grad属性
a = torch.randn(2, 2)
a = ((a * 3) / (a - 1))
print(a.requires_grad)
a.requires_grad_(True)
print(a.requires_grad)
b = (a * a).sum()
print(b.grad_fn)

if __name__ == '__main__':
    pass
