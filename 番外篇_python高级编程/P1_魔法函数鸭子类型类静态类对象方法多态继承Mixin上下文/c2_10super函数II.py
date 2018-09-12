# super函数的调用符合MRO C3算法

class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super(B, self).__init__()

class C(A):
    def __init__(self):
        print("C")
        super(C, self).__init__()

class D(B, C):
    def __init__(self):
        print("D")
        super(D, self).__init__()


if __name__ == '__main__':
    d = D()  # D -> B -> C -> A 完美体现了C3算法
    print(D.__mro__)
    # print(d.__mro__)  # 只有类有 __mro__ 实例没有 