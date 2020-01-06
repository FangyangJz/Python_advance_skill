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

if __name__ == '__main__':
    with pm.Model() as model:
        parameter = pm.Exponential("poisson_param", 1.0)
        data_generator = pm.Poisson("data_generator", parameter)
        data_generator_p1 = data_generator + 1
    print(f"{parameter.tag.test_value}")
    print(f"{data_generator.tag.test_value}, {id(data_generator)}, {id(model)}")
    print(f"{data_generator_p1.tag.test_value}")
    # 下面这两种写法已经在 pymc3 中抛弃了
    # print(f"{data_generator.parents}")
    # print(f"{data_generator.children}")

    with pm.Model() as model:
        theta = pm.Exponential("theta", 2.0)
        data_generator = pm.Poisson("data_generator", theta)
    print(f"{theta.tag.test_value}")
    print(f"{data_generator.tag.test_value}, {id(data_generator)}, {id(model)}")


    # pyro_dist的 snappet 不显示 指数分布, 但是可以通过torch_dist知道有这个类
    parameter_pyro = pyro.sample("poisson_param", pyro_dist.Exponential(1.0))
    data_generator_pyro = pyro.sample("data_generator", pyro_dist.Poisson(parameter_pyro))
    data_generator_pyro_p1 = data_generator_pyro + 1
    print(1)
