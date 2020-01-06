# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2020/1/5 上午1:03
# @Author   : Fangyang
# @Software : PyCharm

import pymc3 as pm
import torch
import pyro.distributions as pyro_dist
import torch.distributions as torch_dist
import pyro
import numpy as np
import theano.tensor as tt
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
from pyro.infer import MCMC, NUTS, HMC
import theano.tensor as tt


def data_check_plot(challenger_data):
    # plot it, as a function of tempature (the first column)
    print("Temp (F), O-Ring failure?")
    print(challenger_data)

    plt.scatter(challenger_data[:, 0], challenger_data[:, 1], s=75, color="k",
                alpha=0.5)
    plt.yticks([0, 1])
    plt.ylabel("Damage Incident?")
    plt.xlabel("Outside temperature (Fahrenheit)")
    plt.title("Defects of the Space Shuttle O-Rings vs temperature")
    plt.show()


def logistic(x, beta, alpha=0):
    return 1.0 / (1.0 + np.exp(np.dot(beta, x) + alpha))


if __name__ == '__main__':
    np.set_printoptions(precision=3, suppress=True)
    challenger_data = np.genfromtxt("./challenger_data.csv", skip_header=1,
                                    usecols=[1, 2], missing_values="NA",
                                    delimiter=",")
    # drop the NA values
    challenger_data = challenger_data[~np.isnan(challenger_data[:, 1])]
    # data_check_plot(challenger_data)

    temperature = challenger_data[:, 0]
    D = challenger_data[:, 1]  # defect or not?

    # notice the`value` here. We explain why below.
    with pm.Model() as model:
        beta = pm.Normal("beta", mu=0, tau=0.001, testval=0)
        alpha = pm.Normal("alpha", mu=0, tau=0.001, testval=0)
        p = pm.Deterministic("p", 1.0 / (1. + tt.exp(beta * temperature + alpha)))

        observed = pm.Bernoulli("bernoulli_obs", p, observed=D)

        # Mysterious code to be explained in Chapter 3
        start = pm.find_MAP()
        step = pm.Metropolis()
        trace = pm.sample(120000, step=step, start=start)
        burned_trace = trace[100000::2]

    alpha_samples = burned_trace["alpha"][:, None]  # best to make them 1d
    beta_samples = burned_trace["beta"][:, None]

    # histogram of the samples:
    plt.subplot(221)
    plt.title(r"Posterior distributions of the variables $\alpha, \beta$")
    plt.hist(beta_samples, histtype='stepfilled', bins=35, alpha=0.85,
             label=r"posterior of $\beta$", color="#7A68A6", normed=True)
    plt.legend()

    plt.subplot(222)
    plt.hist(alpha_samples, histtype='stepfilled', bins=35, alpha=0.85,
             label=r"posterior of $\alpha$", color="#A60628", normed=True)
    plt.legend()

    ###########################################################################
    t = np.linspace(temperature.min() - 5, temperature.max() + 5, 50)[:, None]
    p_t = logistic(t.T, beta_samples, alpha_samples)

    mean_prob_t = p_t.mean(axis=0)

    plt.subplot(223)
    plt.plot(t, mean_prob_t, lw=3, label="average posterior \nprobability \
    of defect")
    plt.plot(t, p_t[0, :], ls="--", label="realization from posterior")
    plt.plot(t, p_t[-2, :], ls="--", label="realization from posterior")
    plt.scatter(temperature, D, color="k", s=50, alpha=0.5)
    plt.title("Posterior expected value of probability of defect; \
    plus realizations")
    plt.legend(loc="lower left")
    plt.ylim(-0.1, 1.1)
    plt.xlim(t.min(), t.max())
    plt.ylabel("probability")
    plt.xlabel("temperature")
    ########################################################################
    from scipy.stats.mstats import mquantiles

    # vectorized bottom and top 2.5% quantiles for "confidence interval"
    qs = mquantiles(p_t, [0.025, 0.975], axis=0)
    plt.subplot(224)
    plt.fill_between(t[:, 0], *qs, alpha=0.7,
                     color="#7A68A6")

    plt.plot(t[:, 0], qs[0], label="95% CI", color="#7A68A6", alpha=0.7)

    plt.plot(t, mean_prob_t, lw=1, ls="--", color="k",
             label="average posterior \nprobability of defect")

    plt.xlim(t.min(), t.max())
    plt.ylim(-0.02, 1.02)
    plt.legend(loc="lower left")
    plt.scatter(temperature, D, color="k", s=50, alpha=0.5)
    plt.xlabel("temp, $t$")

    plt.ylabel("probability estimate")
    plt.title("Posterior probability estimates given temp. $t$");

    plt.show()
    print(1)
