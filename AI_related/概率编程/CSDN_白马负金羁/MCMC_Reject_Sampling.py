# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2020/1/4 下午10:43
# @Author   : Fangyang
# @Software : PyCharm


from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    fig, ax = plt.subplots(1, 2)

    # rvs:随机变量（就是从这个分布中抽一些样本）
    # pdf：概率密度函数。输入x, 得到概率值输出
    # cdf：累计分布函数
    # sf：残存函数（1-CDF）
    # ppf：分位点函数（CDF的逆）, 给出分位点, 得到pdf的x
    # isf：逆残存函数（sf的逆）
    # stats:返回均值，方差，（费舍尔）偏态，（费舍尔）峰度。
    # moment:分布的非中心矩。

    # Inverse CDF 方法
    # https://blog.csdn.net/baimafujinji/article/details/51407703
    x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)
    ax[0].plot(x, norm.pdf(x), 'r-', lw=5, alpha=0.6, label='norm pdf')
    ax[1].plot(x, norm.cdf(x), 'b-', lw=5, alpha=0.6, label='norm pdf')
    plt.show()