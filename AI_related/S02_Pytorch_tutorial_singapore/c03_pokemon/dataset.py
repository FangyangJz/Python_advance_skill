# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/12/6 下午2:31
# @Author   : Fangyang
# @Software : PyCharm

from torch.utils.data import Dataset


class NumberDataset(Dataset):

    def __init__(self, trainning=True):
        if trainning:
            self.samples = list(range(1, 1001))
        else:
            self.samples = list(range(1001, 1501))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, item):
        return self.samples[item]


if __name__ == '__main__':
    a = NumberDataset()
    print(f'a len is {len(a)}')
    print(a[10])
