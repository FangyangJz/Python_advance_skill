# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/11/18
'''
__author__ = 'Fangyang'

# 问题:
# 1. 回调模式编码复杂度高
# 2. 同步编程的并发性不高
# 3. 多线程编程需要线程间同步, lock(会降低并发的性能)

# 理想情况:
# 1. 采用同步的方式编写异步的代码
# 2. 使用单线程去切换任务
#     1> 线程是由操作系统切换的, 单线程切换意味着我们需要自己去调度任务
#     2> 实现了就不在需要锁, 并发性就高, 如果单线程内切换函数, 性能远高于线程切换, 并发性更高

# 我们需要一个可以暂停的函数, 并且可以在适当的时候恢复该函数的继续执行
# 协程 -> 有多个入口的函数, 可以暂停的函数(生成器可以实现), 可以向暂停的地方传入值

def gen_func():
    html = yield 'www.baidu.com'  # 1. 可以产出值;  2. 可以接收值(调用方传递进来的值)
    print(html)
    yield 2
    yield 3
    return 'fangyang'

# 1. 生成器不只可以产出值, 还可以接收值 send



if __name__ == '__main__':
    gen = gen_func()
    # url = gen.send(None)   # 生成器刚开始的时候, 只能发None, 因为还没运行到第一个yield
    # 所以, 在调用send发送非None值之前, 我们必须启动一次生成器, 方式有两种: 1. gen.send(None) 2. next(gen)
    url = next(gen)
    print(url)
    # 1. 启动生成器的方式有两种, next(), send
    html = 'bobby'
    print(gen.send(html))  # send 方法可以传递值进入生成器内部, 同时还可以重启生成器执行到下一个yield位置
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
