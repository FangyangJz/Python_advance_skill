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
    return pyro.sample("measurement", dist.Normal(weight, 1.), obs=9.56)


if __name__ == '__main__':
    # pyro.set_rng_seed(101)
    print(scale_obs(10))
    print(deferred_conditioned_scale(9.5, 2))
    print(1)
