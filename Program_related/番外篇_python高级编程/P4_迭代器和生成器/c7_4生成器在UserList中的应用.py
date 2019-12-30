# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/18
'''
__author__ = 'Fangyang'


from collections import UserList

# 我们自己写的类如果想实现python内部的类型, 比如dict, list...
# 不要去直接继承, 因为list,str,dict这种, 是用C语言写的, 很多不能override
# 用 collections里面的类, 比如 UserList


# 这里讲了个用生成器的例子:
# 500G 单行 大文件 读取
# 用readline读出来都要撑爆内存
# read(4096) 这个函数可以指定一次读取的数量, 再read(4096), 会接着上次的地方继续读

def myreadlines(f, newline):
    buf = ''   # 缓存, 存储已经读出来的数据
    while True:
        while newline in buf:
            pos = buf.index(newline)  # 找到分隔符的位置
            yield buf[:pos]
            buf = buf[pos + len(newline):]

        chunk = f.read(4096*10)
        if not chunk:
            # 说明已经读到了文件结尾
            yield buf
            break
        buf = chunk


if __name__ == '__main__':

    with open('input.txt') as f:
        for line in myreadlines(f, '{|}'):  # '{|}'是分隔符
            print(line)
