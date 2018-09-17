# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/18
'''
__author__ = 'Fangyang'

import dis
import inspect

frame = None

def foo():
    bar()

def bar():
    global frame
    frame = inspect.currentframe()

def gen_func():
    yield 1
    name = 'boo'
    yield 2
    age = 30
    return 'imooc'


if __name__ == '__main__':
    # python.exe 会用PyEval_EvalFramEx(c函数)去执行foo函数,
    # 首先会创建一个栈帧(stack frame) -----上下文, 在栈帧里运行字节码
    # python一切皆对象, 栈帧对象, 字节码对象
    # 当foo调用子函数bar, 又会创建一个栈帧, 然后将控制器交给bar的栈帧
    # 所有的栈帧都是分配在堆内存(不释放就一直存在在内存中)上, 这就决定了栈帧可以独立于调用者存在, 生成器正是利用了这点

    print(dis.dis(foo))  # python 执行前会编译成字节码, 这里用dis看下字节码

    print('-'*50)
    foo()
    print(frame.f_code.co_name)  # 打印出bar的栈帧名字
    caller_frame = frame.f_back
    print(caller_frame.f_code.co_name)

    print('-'*50)
    gen = gen_func()
    print(dis.dis(gen))

    print('='*50)
    print(gen.gi_frame.f_lasti)
    print(gen.gi_frame.f_locals)
    next(gen)
    print(gen.gi_frame.f_lasti)
    print(gen.gi_frame.f_locals)

