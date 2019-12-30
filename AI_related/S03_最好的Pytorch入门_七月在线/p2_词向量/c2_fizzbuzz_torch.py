# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/12/8 下午5:14
# @Author   : Fangyang
# @Software : PyCharm


import numpy as np
import torch
import torch.nn as nn

NUM_DIGITS = 10


def fizz_buzz_encode(i):
    if i % 15 == 0:
        return 3
    elif i % 5 == 0:
        return 2
    elif i % 3 == 0:
        return 1
    else:
        return 0


def binary_encode(i, num_digits):
    return np.array([i >> d & 1 for d in range(num_digits)][::-1])


def fizz_buzz_decode(i, prediction):
    return [str(i), 'fizz', 'buzz', 'fizzbuzz'][prediction]


trX = torch.Tensor([binary_encode(i, NUM_DIGITS) for i in range(101, 2 ** NUM_DIGITS)])
trY = torch.LongTensor([fizz_buzz_encode(i) for i in range(101, 2 ** NUM_DIGITS)])

# x = binary_encode(16, NUM_DIGITS)
# print(x)

NUM_HIDDEN = 100
model = nn.Sequential(
    nn.Linear(NUM_DIGITS, NUM_HIDDEN),
    nn.ReLU(),
    nn.Linear(NUM_HIDDEN, 4)
)

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-2)

BATCH_SIZE = 128
for epoch in range(1000):
    for start in range(0, len(trX), BATCH_SIZE):
        end = start + BATCH_SIZE
        batchX = trX[start:end]
        batchY = trY[start:end]

        y_pred = model(batchX)
        loss = loss_fn(y_pred, batchY)
        print(f'Epoch:{epoch}, loss:{loss.item()}')

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

if __name__ == '__main__':
    testX = torch.Tensor([binary_encode(i, NUM_DIGITS) for i in range(1, 101)])

    with torch.no_grad():
        testY = model(testX)

    predicts = zip(range(1, 101), list(testY.max(1)[1]))
    print([fizz_buzz_decode(i, x) for i,x in predicts])
