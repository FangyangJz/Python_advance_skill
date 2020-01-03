# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/12/29 下午5:40
# @Author   : Fangyang
# @Software : PyCharm

import torch
import pyro


# Define sample model

def weather_torch():
    cloudy = torch.distributions.Bernoulli(0.3).sample()
    cloudy = 'cloudy' if cloudy.item() == 1.0 else 'sunny'
    mean_temp = {'cloudy': 55.0, 'sunny': 75.0}[cloudy]
    scale_temp = {'cloudy': 10.0, 'sunny': 15.0}[cloudy]
    temp = torch.distributions.Normal(mean_temp, scale_temp).rsample()
    return cloudy, temp.item()


def weather_pyro():
    # cloudy = torch.distributions.Bernoulli(0.3).sample()
    cloudy = pyro.sample('cloudy', pyro.distributions.Bernoulli(0.3))
    cloudy = 'cloudy' if cloudy.item() == 1.0 else 'sunny'
    mean_temp = {'cloudy': 55.0, 'sunny': 75.0}[cloudy]
    scale_temp = {'cloudy': 10.0, 'sunny': 15.0}[cloudy]
    # temp = torch.distributions.Normal(mean_temp, scale_temp).rsample()
    temp = pyro.sample('temp', pyro.distributions.Normal(mean_temp, scale_temp))
    return cloudy, temp.item()


def ice_cream_sales(cloudy, temp):
    # cloudy, temp = weather_pyro()
    expected_sales = 200. if cloudy == 'sunny' and temp > 80. else 50.
    ice_cream = pyro.sample('ice_cream', pyro.distributions.Normal(expected_sales, 10.0))
    return ice_cream.item()


if __name__ == '__main__':
    pyro.set_rng_seed(101)
    loc = 0
    scale = 1
    normal = torch.distributions.Normal(loc, scale)
    x = normal.rsample()
    print(x)
    print(normal.log_prob(x))

    for _ in range(3):
        print('-' * 50)
        print("weather torch", weather_torch())
        weather, temperature = weather_pyro()
        print("weather pyro", weather, temperature)
        ice_cream = ice_cream_sales(weather, temperature)
        print("ice cream sales : ", ice_cream)
