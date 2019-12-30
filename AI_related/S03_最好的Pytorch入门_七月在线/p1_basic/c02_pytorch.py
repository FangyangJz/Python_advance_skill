# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/12/7 上午2:18
# @Author   : Fangyang
# @Software : PyCharm


import torch
import numpy as np

# Torch Tensor 和 Numpy array会共享内存, 所以改变其中一项另一项也会变
a = torch.ones(5)
b = a.numpy()
b[1] = 10
print(a, b)

x = np.ones(5)
y = torch.from_numpy(x)
print(x, y)

if torch.cuda.is_available():
    device = torch.device('cuda')
    y = torch.ones(5, device=device)
    x = x.to(device)
    z = x + y
    print(z.to('cpu', torch.double))
    # 转回cpu才能转回numpy,
    # y.cpu().data.numpy()
    # y.to('cpu').data.numpy()

    # model = model.cuda() 模型整个搬到gpu上



if __name__ == '__main__':
    pass
