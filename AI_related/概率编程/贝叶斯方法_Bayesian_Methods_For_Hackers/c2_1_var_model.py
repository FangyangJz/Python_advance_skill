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

if __name__ == '__main__':
    with pm.Model() as model:
        theta_with_testval = pm.Exponential("theta_with_testval", 2.0, testval=0.5)  # theta.tag.test_value, 即初始化值, 可以通过testval指定
        theta_without_testval = pm.Exponential("theta_without_testval", 2.0)  # theta.tag.test_value, 即初始化值, 可以通过testval指定
        data_generator = pm.Poisson("data_generator", theta_with_testval)
    print(f"theta_with_testval.tag.test_value:{theta_with_testval.tag.test_value}")
    print(f"theta_without_testval.tag.test_value:{theta_without_testval.tag.test_value}")
    # print(f"{data_generator.tag.test_value}, {id(data_generator)}, {id(model)}")

    with pm.Model() as ab_testing:
        p_A = pm.Uniform("P(A)", 0, 1)  # 这个产生的都是stochastic类型的变量
        p_B = pm.Uniform("P(B)", 0, 1)
        print(f"p_A.tag.test_value:{p_A.tag.test_value}")
        print(f"p_B.tag.test_value:{p_B.tag.test_value}")

    with pm.Model() as ab_testing_1:
        # 上面分成两句写, 下面这个1句就能生产多个变量
        betas = pm.Uniform("betas", 0, 1, shape=2)  # 必须写在上下文管理器中
        print(f"betas.tag.test_value:{betas.tag.test_value}")


    # Deterministric 类型的变量有两种生成方式
    # 1. 显示定义
    with pm.Model() as model:
        # 必须写在上下文管理器中, 要不报错
        deterministic_variable = pm.Deterministic("deterministic variable", pm.Exponential("lambda_1", 1.0))
    # 2. 隐式定义
    with pm.Model() as model:
        lambda_1 = pm.Exponential("lambda_1", 1.0)
        lambda_2 = pm.Exponential("lambda_2", 1.0)
        tau = pm.DiscreteUniform("tau", lower=0, upper=10)
    new_deterministic_variable = lambda_1 + lambda_2

    n_data_points = 5  # in CH1 we had ~70 data points
    idx = np.arange(n_data_points)
    with model:
        lambda_ = pm.math.switch(tau >= idx, lambda_1, lambda_2)


    # pyro_dist的 snappet 不显示 指数分布, 但是可以通过torch_dist知道有这个类
    # parameter_pyro = pyro.sample("poisson_param", pyro_dist.Exponential(1.0))
    # data_generator_pyro = pyro.sample("data_generator", pyro_dist.Poisson(parameter_pyro))
    # data_generator_pyro_p1 = data_generator_pyro + 1
    # pyro_p_A = torch_dist.Uniform(0, 1)
    # pyro_p_B = torch_dist.Uniform(0, 1)
    print(1)
