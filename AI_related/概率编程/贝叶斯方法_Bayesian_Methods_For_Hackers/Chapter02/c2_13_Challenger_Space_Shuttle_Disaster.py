# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2020/1/5 上午1:03
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
import theano.tensor as tt


if __name__ == '__main__':
    np.set_printoptions(precision=3, suppress=True)
    challenger_data = np.genfromtxt("./challenger_data.csv", skip_header=1,
                                    usecols=[1, 2], missing_values="NA",
                                    delimiter=",")
    # drop the NA values
    challenger_data = challenger_data[~np.isnan(challenger_data[:, 1])]
    # data_check_plot(challenger_data)

    temperature = challenger_data[:, 0]
    D = challenger_data[:, 1]  # defect or not?

    N = 10000
    with pm.Model() as model:
        beta = pm.Normal("beta", mu=0, tau=0.001, testval=0)
        alpha = pm.Normal("alpha", mu=0, tau=0.001, testval=0)
        p = pm.Deterministic("p", 1.0 / (1. + tt.exp(beta * temperature + alpha)))
        observed = pm.Bernoulli("bernoulli_obs", p, observed=D)

        simulated = pm.Bernoulli("bernoulli_sim", p, shape=p.tag.test_value.shape)
        step = pm.Metropolis(vars=[p])
        trace = pm.sample(N, step=step)

    simulations = trace["bernoulli_sim"]
    print(simulations.shape)

    plt.title("Simulated dataset using posterior parameters")
    for i in range(4):
        ax = plt.subplot(4, 1, i + 1)
        plt.scatter(temperature, simulations[1000 * i, :], color="k",
                    s=50, alpha=0.6)
    plt.show()
    print(1)
