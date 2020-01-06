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
    data = np.array([10, 5])
    with pm.Model() as model:
        lambda_1 = pm.Exponential("lambda_1", 1.0)
        fixed_variable = pm.Poisson("fxd", 1, observed=data)
        obs = pm.Poisson("obs", lambda_1, observed=data)

    print(obs.tag.test_value)  # stochastic var has obs
    print("value: ", fixed_variable.tag.test_value)
    print(1)
