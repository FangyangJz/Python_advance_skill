# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/12/7 上午2:18
# @Author   : Fangyang
# @Software : PyCharm


import torch
import numpy as np

x = torch.tensor(1., requires_grad=True)
w = torch.tensor(2., requires_grad=True)
b = torch.tensor(3., requires_grad=True)

y = w * x + b
y.backward()
print(w.grad, x.grad, b.grad)  # dy/dw


if __name__ == '__main__':

    N, D_in, H, D_out = 64, 1000, 100, 10
    x = torch.randn(N, D_in)
    y = torch.randn(N, D_out)

    w1 = torch.randn(D_in, H, requires_grad=True)
    w2 = torch.randn(H, D_out, requires_grad=True)

    learning_rate = 1e-6
    for t in range(500):
        # h = x.mm(w1)
        # h_relu = h.clamp(min=0)
        # y_pred = h_relu.mm(w2)
        y_pred = x.mm(w1).clamp(min=0).mm(w2)

        loss = (y_pred - y).pow(2).sum()
        print(t, loss, loss.item())

        # grad_y_pred = 2.0 * (y_pred - y)
        # grad_w2 = h_relu.t().mm(grad_y_pred)
        # grad_h_relu = grad_y_pred.mm(w2.t())
        # grad_h = grad_h_relu.clone()
        # grad_h[h < 0] = 0
        # grad_w1 = x.t().mm(grad_h)
        loss.backward()

        with torch.no_grad():
            w1 -= learning_rate * w1.grad
            w2 -= learning_rate * w2.grad
            w1.grad.zero_()
            w2.grad.zero_()