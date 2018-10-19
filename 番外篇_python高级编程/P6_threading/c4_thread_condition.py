# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/10/7
'''
__author__ = 'Fangyang'

from threading import Condition, Lock, Thread

# class XiaoAi(Thread):
#     def __init__(self, lock):
#         super().__init__(name='小爱')
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print('{}: 在'.format(self.name))
#         self.lock.release()
#
#
# class TianMao(Thread):
#     def __init__(self, lock):
#         super().__init__(name='天猫精灵')
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print('{}:小爱同学'.format(self.name))
#         self.lock.release()


# 条件变量, 用于复杂的线程间同步
class XiaoAi(Thread):
    def __init__(self, cond):
        super().__init__(name='小爱')
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()   # 等待
            print('{}: 在'.format(self.name))
            self.cond.notify()


class TianMao(Thread):
    def __init__(self, cond):
        super().__init__(name='天猫精灵')
        self.cond = cond

    def run(self):
        with self.cond:   # with 语句相当于 acquire() 然后 release()
            print('{}:小爱同学'.format(self.name))
            self.cond.notify()   # 说完了通知xiaoai
            self.cond.wait()


if __name__ == '__main__':
    cond = Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)

    # 1. 注意启动顺序
    # 2. wait 要在acquire后面
    # condition有两层锁,
    # 一把底层锁会在线程调用了wait方法的时候释放,
    # 上面的锁会在wait的时候分配一把并放入到cond的等待队列中,等到notify方法的唤醒
    xiaoai.start()
    tianmao.start()
