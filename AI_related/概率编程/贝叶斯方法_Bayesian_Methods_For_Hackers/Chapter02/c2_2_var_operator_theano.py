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

if __name__ == '__main__':
    '''
    Here we use theano's stack() function in the same way we would use 
    one of NumPy's stacking functions: to combine our two separate variables, 
    p1 and p2, into a vector with 2 elements. The stochastic categorical variable 
    does not understand what we mean if we pass a NumPy array of p1 and p2 to it 
    because they are both theano variables. Stacking them like this combines them into one 
    theano variable that we can use as the complementary pair of probabilities for our two categories.
    Throughout the course of this book we use several theano functions to help construct our models. 
    If you have more interest in looking at theano itself, be sure to check out the documentation.
    After these technical considerations, we can get back to defining our model!
    '''
    with pm.Model() as theano_test:
        p1 = pm.Uniform("p", 0, 1)
        p2 = 1 - p1
        p = tt.stack([p1, p2])
        # p_np = np.stack([p1, p2])  # 这里要用theano的写法, numpy不对的
        assignment = pm.Categorical("assignment", p)

    print(1)
