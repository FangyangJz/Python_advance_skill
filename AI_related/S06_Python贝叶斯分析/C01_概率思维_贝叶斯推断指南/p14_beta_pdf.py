# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/12/25 下午10:31
# @Author   : Fangyang
# @Software : PyCharm

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

params = [0.5, 1, 2, 3]
x = np.linspace(0, 1, 100)
f, ax = plt.subplots(len(params), len(params), sharex=True, sharey=True)

for i in range(len(params)):
    for j in range(len(params)):
        a = params[i]
        b = params[j]
        y = stats.beta(a, b).pdf(x)
        ax[i, j].plot(x, y)
        ax[i, j].plot(0, 0, label=f"$n$={a:3.2f}\n$p$={b:3.2f}", alpha=0)
        ax[i, j].legend(fontsize=12)


ax[2, 1].set_xlabel("$\\theta$", fontsize=10)
ax[1, 0].set_ylabel("$p(y|\\theta)$", fontsize=10)
# plt.tight_layout()
# ax[0, 0].set_xticks(x)
plt.show()

if __name__ == '__main__':
    pass
