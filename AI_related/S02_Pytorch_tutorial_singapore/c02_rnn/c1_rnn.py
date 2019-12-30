# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/11/29 上午12:04
# @Author   : Fangyang
# @Software : PyCharm

# out = x_t @ W_xh + h_t @ W_hh
# out = [batch, feature_len] @ [hidden_len, feature_len].T()\
#       + [batch, hidden_len] @ [hidden_len, hidden_len].T()
from torch import nn
import torch

rnn = nn.RNN(100, 10)  # (feature_len, mem/hidden_len)
print(rnn._parameters.keys())
# odict_keys(['weight_ih_l0', 'weight_hh_l0', 'bias_ih_l0', 'bias_hh_l0'])
print(rnn.weight_ih_l0.shape, rnn.weight_hh_l0.shape)
# torch.Size([10, 100]) torch.Size([10, 10])


# 100个feature, 记忆20步, 1层
rnn = nn.RNN(input_size=100, hidden_size=20, num_layers=1)
print(rnn)
x = torch.randn(10, 3, 100)  # 每句10个单词, 3个句子(batch), 100 feature
out, h = rnn(x, torch.zeros(1, 3, 20))  # h = [num layer, b, h dim]
print(out.shape, h.shape)  # torch.Size([10, 3, 20]) torch.Size([1, 3, 20])

print('-' * 50)
# 100个feature, 记忆20步, 2层
rnn = nn.RNN(input_size=100, hidden_size=20, num_layers=2)
print(rnn)
x = torch.randn(10, 3, 100)  # 每句10个单词, 3个句子(batch), 100 feature
out, h = rnn(x, torch.zeros(2, 3, 20))  # h = [num layer, b, h dim]
print(out.shape, h.shape)  # torch.Size([10, 3, 20]) torch.Size([1, 3, 20])

print('RNNCell' + "=" * 50)
x = torch.randn(10, 3, 100)  # 每句10个单词, 3个句子(batch), 100 feature
cell1 = nn.RNNCell(100, 20)  # 100 feature, 20 hidden len
h1 = torch.zeros(3, 20)  # 3 batch, 20 hidden len
for xt in x:
    h1 = cell1(xt, h1)  # xt:[3, 100], hl:[3, 20]
print(h1.shape)

print('Tow Layers RNNCell' + "=" * 50)
x = torch.randn(10, 3, 100)  # 每句10个单词, 3个句子(batch), 100 feature
cell1 = nn.RNNCell(100, 30)  # 100 feature, 30 hidden len
cell2 = nn.RNNCell(30, 20)  # 上一层输出的hidden len = 30,  20 hidden len
h1 = torch.zeros(3, 30)  # 3 batch, 30 hidden len
h2 = torch.zeros(3, 20)  # 3 batch, 20 hidden len
for xt in x:
    h1 = cell1(xt, h1)  # xt:[3, 100], cell:[100, 30], h1:[3, 30]
    h2 = cell2(h1, h2)  # h1:[3, 30], cell:[30, 20], h2:[3, 20]
print(h2.shape)

if __name__ == '__main__':
    pass
