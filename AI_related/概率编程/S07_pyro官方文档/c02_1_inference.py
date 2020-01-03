# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/12/29 下午6:37
# @Author   : Fangyang
# @Software : PyCharm


import matplotlib.pyplot as plt
import numpy as np
import torch
import pyro

import pyro.distributions as dist
from torch.distributions import constraints


def scale(guess):
    weight = pyro.sample("weight", dist.Normal(guess, 1.0))
    return pyro.sample("measurement", dist.Normal(weight, 0.75))


def deferred_conditioned_scale(measurement, guess):
    return pyro.condition(scale, data={"measurement": measurement})(guess)


def scale_obs(guess):
    '''
    (Better) equivalent to conditioned_scale above
    '''
    weight = pyro.sample("weight", dist.Normal(guess, 1.))
    # here we condition on measurement == 9.5
    print(f"guess:{guess}' normal generate weight:{weight}")
    return pyro.sample("measurement", dist.Normal(weight, 1.), obs=9.5)


def perfect_guide(guess):
    # 这里的loc和scale是公式推导出来的, 直接给出来weight的后验分布
    loc = (0.75 ** 2 * guess + 0.95) / (1 + 0.75 ** 2)  # 9.14
    scale = np.sqrt(0.75 ** 2 / (1 + 0.75 ** 2))  # 0.6
    return pyro.sample("weight", dist.Normal(loc, scale))


def scale_parametrized_guide_constrained(guess):
    a = pyro.param("a", torch.tensor(guess))
    b = pyro.param("b", torch.tensor(1.), constraint=constraints.positive)
    return pyro.sample("weight", dist.Normal(a, b))  # 上面加了constraints, 要不然这里参数b要写成 torch.abs(b)


if __name__ == '__main__':
    # pyro.set_rng_seed(101)

    # 在已经观察到measurement的条件下, 那么weight就是观测值
    guess = 10
    measurement = 9.5
    print(f"on condition obs=9.5, estimate weight is {scale_obs(10)}")

    print(f"estimate weight is {deferred_conditioned_scale(measurement, guess)}")
    # print(perfect_guide(10))
    print(1)
