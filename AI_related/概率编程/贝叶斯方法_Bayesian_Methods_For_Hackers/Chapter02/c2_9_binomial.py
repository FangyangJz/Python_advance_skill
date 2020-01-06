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
from pyro.infer import MCMC, NUTS, HMC


if __name__ == '__main__':
    binomial = stats.binom

    parameters = [(10, .4), (10, .9)]  # n, p
    colors = ["#348ABD", "#A60628"]

    for i in range(len(parameters)):
        N, p = parameters[i]
        _x = np.arange(N + 1)
        y = binomial.pmf(_x, N, p)
        print(f"_x:{_x}\n N:{N}\n p:{p}\n y:{y}\n\n")
        plt.bar(_x, y, color=colors[i],
                edgecolor=colors[i],
                alpha=0.6,
                label="$N$: %d, $p$: %.1f" % (N, p),
                linewidth=3)

    plt.legend(loc="upper left")
    plt.xlim(0, 10.5)
    plt.xlabel("$k$")
    plt.ylabel("$P(X = k)$")
    plt.title("Probability mass distributions of binomial random variables")
    plt.show()
    print(1)
