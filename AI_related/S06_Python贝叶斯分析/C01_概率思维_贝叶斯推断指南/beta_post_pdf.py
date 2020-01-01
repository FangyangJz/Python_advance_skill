# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/12/25 下午10:31
# @Author   : Fangyang
# @Software : PyCharm

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

theta_real = 0.35
trials = [0, 1, 2, 3, 4, 8, 16, 32, 50, 150] + [3, 4, 5]
data = [0, 1, 1, 1, 1, 4, 6, 9, 13, 48] + [5, 6, 7]

beta_params = [(1, 1), (0.5, 0.5), (20, 20)]
dist = stats.beta
x = np.linspace(0, 1, 100)

col_nums = int(np.ceil(np.sqrt(len(trials))))
x_axis_nums = int(len(trials) / col_nums) + 1
for idx, N in enumerate(trials):

    plt.subplot(x_axis_nums, col_nums, idx + 1)
    y = data[idx]
    for (a_prior, b_prior), c in zip(beta_params, ('b', 'r', 'g')):
        p_theta_given_y = dist.pdf(x, a_prior + y, b_prior + N - y)
        plt.plot(x, p_theta_given_y, c)
        plt.fill_between(x, 0, p_theta_given_y, color=c, alpha=0.6)

    plt.axvline(theta_real, ymax=0.3, color='k')
    plt.plot(0, 0, label=f"{N:d} experiments\n{y:d} heads", alpha=0)
    plt.xlim(0, 1)
    plt.ylim(0, 12)
    plt.xlabel(r"$\theta$")
    plt.ylabel(r"$p(\theta|y)$")
    plt.legend()
    # plt.gca().axes.get_yaxis().set_visible(False)

plt.tight_layout()
plt.show()

if __name__ == '__main__':
    pass
