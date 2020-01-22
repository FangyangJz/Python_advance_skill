# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2020/1/13 下午11:34
# @Author   : Fangyang
# @Software : PyCharm


import pymc3 as pm
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    data_mu = [3e3, 12e3]

    data_std = [5e2, 3e3]

    mu_prior = 35e3
    std_prior = 75e2
    with pm.Model() as model:
        true_price = pm.Normal("true_price", mu=mu_prior, sd=std_prior)

        prize_1 = pm.Normal("first_prize", mu=data_mu[0], sd=data_std[0])
        prize_2 = pm.Normal("second_prize", mu=data_mu[1], sd=data_std[1])
        price_estimate = prize_1 + prize_2

        # logp = pm.Normal.dist(mu=price_estimate, sd=(3e3)).logp(true_price)
        true_price_pdf = pm.Normal.dist(mu=price_estimate, sd=(3e3))
        logp = true_price_pdf.logp(true_price)
        error = pm.Potential("error", logp)

        trace = pm.sample(50000, step=pm.Metropolis())
        burned_trace = trace[10000:]

    price_trace = burned_trace["true_price"]



    x = np.linspace(5000, 40000)
    plt.plot(x, stats.norm.pdf(x, 35000, 7500), c="k", lw=2,
             label="prior dist. of suite price")

    _hist = plt.hist(price_trace, bins=35, normed=True, histtype="stepfilled")
    plt.title("Posterior of the true price estimate")
    plt.vlines(mu_prior, 0, 1.1 * np.max(_hist[0]), label="prior's mean",
               linestyles="--")
    plt.vlines(price_trace.mean(), 0, 1.1 * np.max(_hist[0]), \
               label="posterior's mean", linestyles="-.")
    plt.legend(loc="upper left")
    plt.show()
