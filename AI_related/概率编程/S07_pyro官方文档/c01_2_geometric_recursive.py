# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/12/29 下午5:40
# @Author   : Fangyang
# @Software : PyCharm

import torch
import pyro


def geometric(p, t=None):
    if t is None:
        t = 0
    x = pyro.sample(f"x_{t}", pyro.distributions.Bernoulli(p))
    print(f"x_{t}", x.item())
    if x.item() == 1:
        return 0
    else:
        return 1 + geometric(p, t + 1)


if __name__ == '__main__':
    # pyro.set_rng_seed(101)
    print(geometric(0.5))
