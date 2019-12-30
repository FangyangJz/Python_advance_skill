# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/12/7 上午2:18
# @Author   : Fangyang
# @Software : PyCharm


import torch

x = torch.rand(5, 3)
print(x, x.dtype)
x1 = x.new_ones(3, 3, dtype=torch.double)  # 从一个已有的tensor构建一个tensor
print(x1, x1.dtype)
x2 = torch.randn_like(x1)
print(x2, x2.dtype)

x = torch.tensor([1, 2, 3])
y = torch.tensor([2, 2, 2])
print(y.add_(x))  # in-place 加法, 类似的还有x.copy_(y), x.t_() 都会改变x
print(y)

x_view = x.view(-1, 1)
# x_view = x.view(1, 3)
# x_view = x.view(3)
print(x_view)
x_data = x.data
print(x_data, x[0].item())
print(x.grad)

if __name__ == '__main__':
    pass
