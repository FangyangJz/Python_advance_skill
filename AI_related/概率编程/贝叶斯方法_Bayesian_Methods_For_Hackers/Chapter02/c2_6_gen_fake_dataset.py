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


def plot_artificial_sms_dataset():
    tau = stats.randint.rvs(0, 80)
    alpha = 1. / 20.
    # 另一种等价写法
    # lambda_1, lambda_2 = np.random.exponential(scale=1 / alpha, size=2)
    lambda_1, lambda_2 = stats.expon.rvs(scale=1 / alpha, size=2)
    data = np.r_[stats.poisson.rvs(mu=lambda_1, size=tau), stats.poisson.rvs(mu=lambda_2, size=80 - tau)]
    plt.bar(np.arange(80), data, color="#348ABD")
    plt.bar(tau - 1, data[tau - 1], color="r", label="user behaviour changed")
    plt.xlim(0, 80)


if __name__ == '__main__':

    plt.title("More example of artificial datasets")
    for i in range(4):
        plt.subplot(4, 1, i + 1)
        plot_artificial_sms_dataset()
    plt.show()
    print(1)
