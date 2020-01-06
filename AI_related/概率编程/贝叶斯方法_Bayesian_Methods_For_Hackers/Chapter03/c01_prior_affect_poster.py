# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2020/1/6 下午11:47
# @Author   : Fangyang
# @Software : PyCharm

import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # create the observed data
    # sample size of data we observe, trying varying this (keep it less than 100 ;)
    N = 1

    # the true parameters, but of course we do not see these values...
    lambda_1_true = 1
    lambda_2_true = 3

    # ...we see the data generated, dependent on the above two values.
    # check_temp_var = stats.poisson.rvs(lambda_1_true, size=(N, 1))
    data = np.concatenate([
        stats.poisson.rvs(lambda_1_true, size=(N, 1)),
        stats.poisson.rvs(lambda_2_true, size=(N, 1))
    ], axis=1)
    print("observed (2-dimensional,sample size = %d):" % N, data)

    # plotting details.
    x = y = np.linspace(.01, 5, 100)
    ######################################################
    # .prod 这里实际上是将(100,1)shape的矩阵, 变为(100,)
    # 相当于做了.flatten(), 辣鸡啊
    ########################################################
    likelihood_x = np.array([stats.poisson.pmf(data[:, 0], _x)
                             for _x in x]).prod(axis=1)
    likelihood_y = np.array([stats.poisson.pmf(data[:, 1], _y)
                             for _y in y]).prod(axis=1)
    # L 相当于把假设的2个参数的分布组合平面的真实值表示出来
    L = np.dot(likelihood_x[:, None], likelihood_y[None, :])
    # 相当于上面这句
    # L2 = np.dot(likelihood_x.reshape(-1, 1), likelihood_y.reshape(1, -1))

    ######################################################
    jet = plt.cm.jet
    # matplotlib heavy lifting below, beware!
    plt.subplot(221)
    uni_x = stats.uniform.pdf(x, loc=0, scale=5)
    uni_y = stats.uniform.pdf(x, loc=0, scale=5)
    M = np.dot(uni_x[:, None], uni_y[None, :])
    im = plt.imshow(M, interpolation='none', origin='lower',
                    cmap=jet, vmax=1, vmin=-.15, extent=(0, 5, 0, 5))
    plt.scatter(lambda_2_true, lambda_1_true, c="k", s=50, edgecolor="none")
    plt.xlim(0, 5)
    plt.ylim(0, 5)
    plt.title("Landscape formed by Uniform priors on $p_1, p_2$.")
    #####################################################
    plt.subplot(223)
    plt.contour(x, y, M * L)
    im = plt.imshow(M * L, interpolation='none', origin='lower',
                    cmap=jet, extent=(0, 5, 0, 5))
    plt.title("Landscape warped by %d data observation;\n Uniform priors on $p_1, p_2$." % N)
    plt.scatter(lambda_2_true, lambda_1_true, c="k", s=50, edgecolor="none")
    plt.xlim(0, 5)
    plt.ylim(0, 5)
    #####################################################
    plt.subplot(222)
    exp_x = stats.expon.pdf(x, loc=0, scale=3)
    exp_y = stats.expon.pdf(x, loc=0, scale=10)
    M = np.dot(exp_x[:, None], exp_y[None, :])

    plt.contour(x, y, M)
    im = plt.imshow(M, interpolation='none', origin='lower',
                    cmap=jet, extent=(0, 5, 0, 5))
    plt.scatter(lambda_2_true, lambda_1_true, c="k", s=50, edgecolor="none")
    plt.xlim(0, 5)
    plt.ylim(0, 5)
    plt.title("Landscape formed by Exponential priors on $p_1, p_2$.")

    plt.subplot(224)
    # This is the likelihood times prior, that results in the posterior.
    plt.contour(x, y, M * L)
    im = plt.imshow(M * L, interpolation='none', origin='lower',
                    cmap=jet, extent=(0, 5, 0, 5))

    plt.scatter(lambda_2_true, lambda_1_true, c="k", s=50, edgecolor="none")
    plt.title("Landscape warped by %d data observation;\n Exponential priors on \
    $p_1, p_2$." % N)
    plt.xlim(0, 5)
    plt.ylim(0, 5)
    plt.show()

