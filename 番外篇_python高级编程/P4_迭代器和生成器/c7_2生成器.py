
# 生成器函数, 只要函数里有yield关键字
def gen_func():
    yield 1
    yield 2  # 和return不同, 后面的yield会被执行, 惰性求值得特点决定的
    yield 3


def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index-1) + fib(index-2)

def fib2(index):   # 缺点太消耗内存了当数据量大的时候
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
        re_list.append(b)
        a, b = b, a+b
        n += 1
    return re_list

def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a+b
        n += 1


if __name__=='__main__':
    gen = gen_func()  # 返回的是generator对象, python编译字节码的时候就生成了
    # 生成器符合迭代器协议, 所以可以用for循环访问
    for i in gen:
        print(i)

    print(fib(10))                # 1. 只能看到终值, 看不到过程
    print(fib2(11))             # 2. 都能看到, 但是消耗内存
    for data in gen_fib(12):  # 3. 都能看到, 不消耗内存
        print(data, end=',')