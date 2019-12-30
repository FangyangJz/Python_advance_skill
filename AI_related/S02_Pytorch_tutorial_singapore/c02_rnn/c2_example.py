# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/11/29 上午12:57
# @Author   : Fangyang
# @Software : PyCharm


import torch
import numpy as np
from torch import nn, optim


class Net(nn.Module):
    def __init__(self,
                 input_size: int, hidden_size: int, num_layers: int,
                 batch_first: bool, output_size: int):
        super(Net, self).__init__()
        self.rnn = nn.RNN(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=batch_first  # True: [b, seq, feature], False:[seq, b, feature]
        )
        self.hidden_size = hidden_size
        self.linear = nn.Linear(hidden_size, output_size)

    def forward(self, x, hidden_prev):
        out, hidden_prev = self.rnn(x, hidden_prev)  # [1, seq, h] => [seq, h]
        out = out.view(-1, self.hidden_size)
        out = self.linear(out)  # [seq, h] => [seq, output_size]
        out = out.unsqueeze(dim=0)  # => [1, seq, 1]
        return out, hidden_prev


hidden_size = 10
input_size = 1  # feature len
model = Net(input_size=input_size, hidden_size=hidden_size, num_layers=1, batch_first=True, output_size=1)
print(model)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

num_time_steps = 100
hidden_prev = torch.zeros(1, 1, hidden_size)
for iter in range(2000):
    start = np.random.randint(10, size=1)[0]  # 0/1/2.../9
    time_steps = np.linspace(start, start + 10, num_time_steps)
    data = np.sin(time_steps).reshape(-1, 1)
    # y 是 x后1天
    x = torch.tensor(data[:-1]).float().view(1, num_time_steps - 1, 1)
    y = torch.tensor(data[1:]).float().view(1, -1, 1)

    output, hidden_prev = model(x, hidden_prev)
    hidden_prev = hidden_prev.detach()

    loss = criterion(output, y)
    model.zero_grad()
    loss.backward()
    for p in model.parameters():
        print(p.grad.norm())   # print看到非常大的时候, 发生梯度爆炸, 用下面这句clip
    # [torch.nn.utils.clip_grad_norm_(p, 10) for p in model.parameters()]  ## Gradient Clipping 防止梯度爆炸, 梯度消失可以采用LSTM
    optimizer.step()

    if iter % 100 == 0:
        print(f"Iteration: {iter}, loss: {loss.item()}")

if __name__ == '__main__':
    # predict
    predictions = []
    input = x[:, 1, :]  # 取 n/第n 个点作为起始点x 送进模型预测
    for _ in range(x.shape[1]):
        input = input.view(1, -1, 1)
        pred, hidden_prev = model(input, hidden_prev)
        input = pred
        predictions.append(pred.detach().numpy().ravel()[0])
    print(1)

    import matplotlib.pyplot as plt
    axis_x = range(len(x.numpy().flatten()))
    plt.plot(axis_x, y.numpy().flatten())
    plt.plot(axis_x, predictions)
    plt.show()
