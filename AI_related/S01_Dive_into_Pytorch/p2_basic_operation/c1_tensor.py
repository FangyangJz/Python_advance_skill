# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/12/22 下午11:10
# @Author   : Fangyang
# @Software : PyCharm

import torch

# a = torch.arange(2,10,2)
# b = torch.linspace(2,10,100)
# print(a, b)
# c = torch.randperm(10)
# print(c)

a = torch.linspace(1, 10, 20).view(4, 5)
print(a)
tensor_index = torch.tensor([0, 3])
b = torch.index_select(a, 0, tensor_index)  # 在0维(行)上取0,3行数据
c = torch.index_select(a, 1, tensor_index)  # 在1维(列)上取0,3列数据
print(a, b, c, sep=f'\n{"*" * 20}\n')

d = torch.eye(3, 3)
print(d, torch.nonzero(d))  # 返回非零元素的下标
mask_tensor = d.eq(1)
print(mask_tensor)
e = torch.masked_select(d, mask=torch.tensor([[False, False, True], [False, False, False], [False, False, False]],
                                             dtype=bool))
print(e)
e = torch.masked_select(d, mask=mask_tensor)
print(e)

x = torch.tensor([1, 2, 3, 4, 5, 6])
x_cp = x.clone().view(-1, 2)
x1 = x.view(-1, 2)
x += 1
print(x, x1, x_cp)

if __name__ == '__main__':
    pass
