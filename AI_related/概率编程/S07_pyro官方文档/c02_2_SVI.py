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


def scale_parametrized_guide_constrained(guess):
    a = pyro.param("a", torch.tensor(guess))
    b = pyro.param("b", torch.tensor(1.), constraint=constraints.positive)
    return pyro.sample("weight", dist.BetaBinomial(a, b))  # 上面加了constraints, 要不然这里参数b要写成 torch.abs(b)


if __name__ == '__main__':
    pyro.set_rng_seed(101)

    guess = 9.5
    measurement = 9.5

    pyro.clear_param_store()
    conditioned_scale = pyro.condition(scale, data={"measurement": measurement})
    svi = pyro.infer.SVI(
        model=conditioned_scale,
        guide=scale_parametrized_guide_constrained,
        optim=pyro.optim.SGD({"lr": 0.001, "momentum": 0.1}),
        loss=pyro.infer.Trace_ELBO()
    )

    losses, a, b = [], [], []
    num_steps = 2500
    for t in range(num_steps):
        losses.append(svi.step(guess))
        ele_a, ele_b = pyro.param("a").item(), pyro.param("b").item()
        a.append(ele_a)
        b.append(ele_b)

    plt.plot(losses)
    plt.title("ELBO")
    plt.xlabel("step")
    plt.ylabel("loss")
    print(f"a={ele_a}, b={ele_b}")
    plt.show()
    print(1)
