# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/8/21
'''

__author__ = 'Fangyang'

# 实现一个web框架, 集成cache(redis, cache, memorycache)
# 需要设计一个抽象基类, 指定子类 强制 实现某种方法
# 如何去模拟这样一个抽象基类

# 注意! abc方法很少会使用, 也不推荐, 这里就是加深鸭子类型的理解
# 推荐的方法是 Mixin??

import abc

class CacheBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass

# 子类
class RedisCache(CacheBase):
    def set(self, key, value):
        pass


# 没有在子类中实现get方法, 这里就会报错了
redis_cache = RedisCache()


# python中一些常用的抽象基类, 在collection.abc模块中
from collections.abc import *