# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/12/24 下午6:26
# @Author   : Fangyang
# @Software : PyCharm

import torch
import matplotlib.pyplot as plt
import numpy as np
import random

input_dim = 2
num_examples = 1000
true_w = [2, -3.4]
true_b = 4.2
features = torch.from_numpy(np.random.normal(0, 1, (num_examples, input_dim)))
labels = true_w[0] * features[:, 0] + true_w[1] * features[:, 1] + true_b
labels += torch.from_numpy(np.random.normal(0, 0.01, size=(labels.size())))


# print(features[0], labels[0])


# plt.scatter(features[:,1].numpy(), labels.numpy())
# plt.show()

def data_iter(batch_size, features, labels):
    num_examples = len(features)
    indices = list(range(num_examples))
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        j = torch.LongTensor(indices[i:min(i + batch_size, num_examples)])
        yield features.index_select(0, j), labels.index_select(0, j)  # 0代表维度


def linreg(X, w, b):
    return torch.mm(X, w) + b


def squared_loss(y_hat, y):
    return (y_hat - y.view(y_hat.size())) ** 2 / 2


def sgd(params, lr, batch_size):
    for param in params:
        param.data -= lr * param.grad / batch_size


w = torch.tensor(np.random.normal(0, 0.01, (input_dim, 1)), dtype=torch.float64)
b = torch.zeros(1, dtype=torch.float64)
w.requires_grad_()
b.requires_grad_()

batch_size = 10

lr = 0.03
num_epochs = 10
net = linreg
loss = squared_loss

for epoch in range(num_epochs):

    for X, y in data_iter(batch_size, features, labels):
        # print(X, y)
        # break
        l = loss(net(X, w, b), y).sum()
        l.backward()
        sgd([w, b], lr, batch_size)

        w.grad.data.zero_()
        b.grad.data.zero_()
    train_l = loss(net(features, w, b), labels)
    print(f"epoch : {epoch + 1}, loss : {train_l.mean().item()}")

print(f"true_w : {true_w}, w : {w}")
print(f"true_b : {true_b}, w : {b}")

if __name__ == '__main__':
    pass
