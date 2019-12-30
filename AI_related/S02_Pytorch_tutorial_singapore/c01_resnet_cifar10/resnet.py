# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/11/26 下午4:36
# @Author   : Fangyang
# @Software : PyCharm

import torch
from torch import nn
from torch.nn import functional as F


class ResBlk(nn.Module):

    def __init__(self, ch_in, ch_out, stride):
        super(ResBlk, self).__init__()
        self.conv1 = nn.Conv2d(ch_in, ch_out, kernel_size=3, stride=stride, padding=1)
        self.batch_norm1 = nn.BatchNorm2d(ch_out)
        self.conv2 = nn.Conv2d(ch_out, ch_out, kernel_size=3, stride=1, padding=1)
        self.batch_norm2 = nn.BatchNorm2d(ch_out)

        self.extra = nn.Sequential()
        if ch_out != ch_in:
            self.extra = nn.Sequential(
                nn.Conv2d(ch_in, ch_out, kernel_size=1, stride=stride),
                nn.BatchNorm2d(ch_out)
            )

    def forward(self, x):
        '''

        :param x: [b, ch, h, w]
        :return:
        '''
        out = F.relu(self.batch_norm1(self.conv1(x)))
        out = self.batch_norm2(self.conv2(out))
        # short cut
        # x: [b, ch_in, h, w] , out:[b, ch_out, h, w]

        out = self.extra(x) + out
        return out


class ResNet18(nn.Module):
    def __init__(self):
        super(ResNet18, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(64)
        )
        # followed 4 blocks
        # [b, 64, h, w] => [b, 128, h, w]
        self.block_group = nn.Sequential(
            ResBlk(64, 128),
            ResBlk(128, 256),
            ResBlk(256, 512),
            ResBlk(512, 1024)
        )
        self.outlayer = nn.Linear(1024, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.block_group(x)
        x = self.outlayer(x)
        return x


if __name__ == '__main__':
    blk = ResBlk(64, 128, stride=1)
    temp = torch.randn(2, 64, 32, 32)
    out = blk(temp)
    print(f'out.shape : {out.shape}')