# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2020/1/6 下午11:47
# @Author   : Fangyang
# @Software : PyCharm

import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import pymc3 as pm
import theano.tensor as T

if __name__ == '__main__':
    data = np.loadtxt("data/mixture_data.csv", delimiter=",")

    with pm.Model() as model:
        p1 = pm.Uniform('p', 0, 1)
        p2 = 1 - p1
        # Unfortunately, we can't we just give [p1, p2] to our Categorical variable.
        # PyMC3 uses Theano under the hood to construct the models
        # so we need to use theano.tensor.stack() to combine p1 and p2
        # into a vector that it can understand.
        # We pass this vector into the Categorical variable as well as the testval parameter
        # to give our variable an idea of where to start from.
        p = T.stack([p1, p2])
        testval = np.random.randint(0, 2, data.shape[0])
        print(f"testval[:10] is {testval[:10]}")
        assignment = pm.Categorical("assignment", p,
                                    shape=data.shape[0],
                                    testval=testval)

    print("prior assignment, with p = %.2f:" % p1.tag.test_value)
    print(assignment.tag.test_value[:10])

    with model:
        sds = pm.Uniform("sds", 0, 100, shape=2)
        centers = pm.Normal("centers",
                            mu=np.array([120, 190]),
                            sd=np.array([10, 10]),
                            shape=2)

        center_i = pm.Deterministic('center_i', centers[assignment])
        sd_i = pm.Deterministic('sd_i', sds[assignment])

        # and to combine it with the observations:
        observations = pm.Normal("obs", mu=center_i, sd=sd_i, observed=data)

    print("Random assignments: ", assignment.tag.test_value[:4], "...")
    print("Assigned center: ", center_i.tag.test_value[:4], "...")
    print("Assigned standard deviation: ", sd_i.tag.test_value[:4])

    with model:
        step1 = pm.Metropolis(vars=[p, sds, centers])
        # step2 = pm.ElemwiseCategorical(vars=[assignment])
        step2 = pm.CategoricalGibbsMetropolis(vars=[assignment])
        trace = pm.sample(5000, step=[step1, step2])
        #  in this case Metropolis() for our continuous variables
        #  and ElemwiseCategorical() for our categorical variable.
        #  We will use these sampling methods together
        #  to explore the space by using sample( iterations, step ),
        #  where iterations is the number of steps you wish the algorithm to perform
        #  and step is the way in which you want to handle those steps.
        #  We use our combination of Metropolis() and ElemwiseCategorical()
        #  for the step and sample 25000 iterations below.

    ##############################################
    plt.subplot(311)
    lw = 1
    center_trace = trace["centers"]

    # for pretty colors later in the book.
    colors = ["#348ABD", "#A60628"] if center_trace[-1, 0] > center_trace[-1, 1] \
        else ["#A60628", "#348ABD"]

    plt.plot(center_trace[:, 0], label="trace of center 0", c=colors[0], lw=lw)
    plt.plot(center_trace[:, 1], label="trace of center 1", c=colors[1], lw=lw)
    plt.title("Traces of unknown parameters")
    leg = plt.legend(loc="upper right")
    leg.get_frame().set_alpha(0.7)

    plt.subplot(312)
    std_trace = trace["sds"]
    plt.plot(std_trace[:, 0], label="trace of standard deviation of cluster 0",
             c=colors[0], lw=lw)
    plt.plot(std_trace[:, 1], label="trace of standard deviation of cluster 1",
             c=colors[1], lw=lw)
    plt.legend(loc="upper left")

    plt.subplot(313)
    p_trace = trace["p"]
    plt.plot(p_trace, label="$p$: frequency of assignment to cluster 0",
             color=colors[0], lw=lw)
    plt.xlabel("Steps")
    plt.ylim(0, 1)
    # 这个画legend的方式挺有意思
    leg = plt.legend(loc="upper right")
    leg.get_frame().set_alpha(0.8)
    plt.show()

    # 可以追加mcmc的次数, 在上面trace的基础上
    # 这个特点在jupyter中比较好用
    # with model:
    #     trace = pm.sample(50000, step=[step1, step2], trace=trace)
