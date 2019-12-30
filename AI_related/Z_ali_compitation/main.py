# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/12/26 上午3:12
# @Author   : Fangyang
# @Software : PyCharm

import pandas as pd
import torch.utils.data as Data
import torch.nn as nn
import torch
import numpy as np


class LinearNet(nn.Module):
    def __init__(self, n_feature):
        super(LinearNet, self).__init__()
        self.linear = nn.Sequential(
            nn.Linear(n_feature, 512),
            nn.ReLU(),
            nn.Linear(512, 1024),
            nn.ReLU(),
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Linear(512, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 1),
        )

    def forward(self, x):
        y = self.linear(x)
        return y


if __name__ == '__main__':
    df = pd.read_csv("zhengqi_train.txt", sep='\t')
    check = df.iloc[:, :-1].apply(lambda x: (x - x.mean()) / x.std())
    feature_df = torch.from_numpy(df.iloc[:, :-1].apply(lambda x: (x - x.mean()) / x.std()).values)
    labels_s = torch.from_numpy(df.iloc[:, -1].values)
    dataset = Data.TensorDataset(feature_df, labels_s)
    data_iter = Data.DataLoader(dataset, batch_size=10, shuffle=True)

    net = LinearNet(feature_df.shape[1])
    net = net.double()
    print(net)

    criteron = nn.MSELoss()
    optimizer = torch.optim.Adam(net.parameters(), lr=1e-3)

    for epoch in range(100):
        net.train()
        for x, label in data_iter:
            output = net(x)
            loss = criteron(output, label)

            # backpropagation
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        print(f"epoch : {epoch}, loss : {loss}")

    print(1)
