# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/11/18
'''
__author__ = 'Fangyang'


import os
import time
from concurrent.futures import ProcessPoolExecutor  # 这个更上面一点, 推荐使用
import multiprocessing  # 这个更底层


# pid = os.fork()  # 只能用于linux
# print('boddy')
# if pid == 0:  # 子进程中 pid == 0
#     print('子进程:{}, 父进程:{}'.format(os.getpid(), os.getppid()))
# else:
#     print('I am parent process : {}'.format(pid))
#
# time.sleep(2)  # 这里是为了等待子进程完成, 要不父进程一下就结束了

def get_html(n):
    time.sleep(n)
    print('sub process success!')
    return n

# class MyProcess(multiprocessing.Process):
#     def run(self):
#         pass


if __name__ == '__main__':
    # process = multiprocessing.Process(target=get_html, args=(2, ))
    # print(process.pid)  # 进程有个属性 pid, start后才有
    # process.start()
    # print(process.pid)
    # process.join()
    # print('main process end')

    # 使用进程池
    # pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_html, args=(3, ))
    # pool.close()  # 在join前必须close掉pool, 不让进程池接收新的任务进来
    # pool.join()   # 等待所有任务完成
    # print(result.get())

    # imap
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    for result in pool.imap(get_html, [1, 5, 3]):
        print('{} sleep success'.format(result))

    for result in pool.imap_unordered(get_html, [1, 5, 3]):
        print('{} sleep success'.format(result))