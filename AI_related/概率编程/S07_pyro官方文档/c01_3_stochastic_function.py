# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/12/29 下午5:40
# @Author   : Fangyang
# @Software : PyCharm

import torch
import pyro


def normal_product(loc, scale):
    z1 = pyro.sample("z1", pyro.distributions.Normal(loc, scale))
    z2 = pyro.sample("z2", pyro.distributions.Normal(loc, scale))
    return z1 * z2


def make_normal_normal():
    mu_latent = pyro.sample("mu_latent", pyro.distributions.Normal(0, 1))
    fn = lambda scale: normal_product(mu_latent, scale)
    return fn


if __name__ == '__main__':
    # pyro.set_rng_seed(101)
    print(make_normal_normal()(1.0))
