# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2020/1/3 下午10:24
# @Author   : Fangyang
# @Software : PyCharm


import pymc3 as pm
import torch
import pyro.distributions as pyro_dist
import torch.distributions as torch_dist
import pyro
import numpy as np
import theano.tensor as tt
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd

if __name__ == '__main__':
    tau = np.random.randint(0, 80)
    print(tau)

    alpha = 1. / 20.
    lambda_1, lambda_2 = np.random.exponential(scale=1 / alpha, size=2)
    print(lambda_1, lambda_2)

    # np.r_ 用法
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = np.c_[a, b]
    print(np.r_[a, b])
    print(np.c_[c, a])

    data = np.r_[stats.poisson.rvs(mu=lambda_1, size=tau), stats.poisson.rvs(mu=lambda_2, size=80 - tau)]
    print(data)

    plt.bar(np.arange(80), data, color="b")
    plt.bar(tau - 1, data[tau - 1], color="r", label="user behaviour changed")
    plt.xlabel("Time (days)")
    plt.ylabel("count of text-msgs received")
    plt.title("Artificial dataset")
    plt.xlim(0, 80)
    plt.legend()
    plt.show()
    print(1)
