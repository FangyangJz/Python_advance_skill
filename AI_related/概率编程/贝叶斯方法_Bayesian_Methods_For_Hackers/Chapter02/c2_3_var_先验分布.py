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
    # figsize(12.5, 4)
    with pm.Model() as model:
        lambda_1 = pm.Exponential("lambda_1", 1.0)
        lambda_2 = pm.Exponential("lambda_2", 1.0)
        tau = pm.DiscreteUniform("tau", lower=0, upper=10)
    new_deterministic_variable = lambda_1 + lambda_2

    samples = lambda_1.random(size=20000)

    up_bound = 10
    low_bound = -10
    x_axis = torch.linspace(low_bound, up_bound, 20000).detach()
    x_axis_random = torch.from_numpy(np.random.random(20000) * up_bound)
    # log_prob(value) , 是对分布上value的概率值取了log, 然后用exp对其还原回prob
    # exp_param_with_sequence = pyro.distributions.Exponential(1.0).log_prob(x_axis).exp().numpy()
    # tt_tensor = torch.tensor([20000])
    # tt_Tensor = torch.Tensor([20000])
    # tt_tensor_0 = torch.tensor(20000)
    # tt_Tensor_0 = torch.Tensor(20000)
    #######################################################################
    # pymc3 sample 等价 pyro 写法
    exp_param_with_sequence0 = pyro.distributions.Exponential(1.0).sample(torch.tensor([20000])).numpy()  # tensor 20000不加.生成的类型是int64
    exp_param_with_sequence1 = pyro.distributions.Exponential(1.0).sample(torch.Tensor(20000).size()).numpy()  # Tensor 加不加点, 生成类型是float32
    ######################################################################
    # 这里是对指定区间采样的写法探索
    exp_param_with_random0 = pyro.distributions.Exponential(1.0).log_prob(x_axis).exp().numpy()
    exp_param_with_random1 = pyro.distributions.Exponential(1.0).log_prob(x_axis_random).exp().numpy()
    # lambda_1_pyro = pyro.sample("lambda_1_pyro", exp_param)
    #####################################################################

    df = pd.DataFrame()
    df['samples'] = samples
    df['exp_param_with_sequence0'] = exp_param_with_sequence0
    df['exp_param_with_sequence1'] = exp_param_with_sequence1
    df['exp_param_with_random0'] = exp_param_with_random0
    df['exp_param_with_random1'] = exp_param_with_random1
    print(df.info())
    df_desc = df.describe()
    for i in df_desc:
        print(df_desc[i])

    #########################################
    # 画图这里如果是二维数组, ax表示这么写
    # f, ax = plt.subplots(2, 2)
    # ax[0, 0].hist(samples, bins=70, normed=True, histtype="stepfilled")
    # ax[1, 0].hist(samples, bins=70, density=True, histtype="stepfilled")
    # ax[0, 1].hist(samples, bins=70, normed=True, histtype="stepfilled")
    ###########################################

    # 如果是1维数组图, 用这么写
    f, ax1 = plt.subplots(5, 1)
    ax1[0].hist(samples, bins=70, normed=True, histtype="stepfilled")
    ax1[1].hist(exp_param_with_sequence0, bins=70, density=True, histtype="stepfilled")
    ax1[2].hist(exp_param_with_sequence1, bins=70, density=True, histtype="stepfilled")
    ax1[3].hist(exp_param_with_random0, bins=70, density=True, histtype="stepfilled")
    ax1[4].hist(exp_param_with_random1, bins=70, density=True, histtype="stepfilled")

    # plt.title("Prior distribution for $\lambda_1$")
    # plt.xlim(0, 8)
    plt.show()
    print(1)
