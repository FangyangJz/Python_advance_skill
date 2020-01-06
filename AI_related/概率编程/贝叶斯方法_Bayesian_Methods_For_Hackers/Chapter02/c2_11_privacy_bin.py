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
import theano.tensor as tt

if __name__ == '__main__':
    N = 100
    with pm.Model() as model:
        p = pm.Uniform("freq_cheating", 0, 1)
        # I could have typed p_skewed = 0.5*p + 0.25 instead for a one-liner,
        # as the elementary operations of addition and scalar multiplication
        # will implicitly create a deterministic variable,
        # but I wanted to make the deterministic boilerplate explicit for clarity's sake.
        #
        # If we know the probability of respondents saying "Yes", which is p_skewed, and we have
        # N=100 students, the number of "Yes" responses is a binomial random variable with parameters N and p_skewed.
        #
        # This is where we include our observed 35 "Yes" responses.
        # In the declaration of the pm.Binomial, we include value = 35 and observed = True.
        p_skewed = pm.Deterministic("p_skewed", 0.5 * p + 0.25)
        yes_responses = pm.Binomial("number_cheaters", N, p_skewed, observed=35)

        # To Be Explained in Chapter 3!
        step = pm.Metropolis()
        trace = pm.sample(25000, step=step)
        burned_trace = trace[2500:]
    p_trace = burned_trace["freq_cheating"]
    plt.hist(p_trace, histtype="stepfilled", normed=True, alpha=0.85, bins=30,
             label="posterior distribution", color="#348ABD")
    plt.vlines([.05, .35], [0, 0], [5, 5], alpha=0.2)
    plt.xlim(0, 1)
    plt.legend()
    plt.show()
    print(1)
