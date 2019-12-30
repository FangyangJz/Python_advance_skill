# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/12/26 上午12:18
# @Author   : Fangyang
# @Software : PyCharm

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns


def naive_hpd(post):
    sns.kdeplot(post)
    HPD = np.percentile(post, [2.5, 97.5])  # 95% HPD
    plt.plot(HPD, [0, 0], label="HPD {:.2f} {:.2f}".format(*HPD), lw=8, color='k')
    plt.legend(fontsize=16)
    plt.xlabel(r"$\theta$", fontsize=14)
    plt.gca().axes.get_yaxis().set_ticks([])


np.random.seed(1)
post = stats.beta.rvs(5, 11, size=1000)
naive_hpd(post)
plt.xlim(0, 1)
plt.show()

if __name__ == '__main__':
    pass
