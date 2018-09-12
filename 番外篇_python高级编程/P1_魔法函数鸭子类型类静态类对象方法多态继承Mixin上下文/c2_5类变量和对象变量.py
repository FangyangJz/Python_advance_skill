class A:
    aa = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = A(2,3)
print(a.x, a.y, a.aa)

a.aa = 100   # 实际在 __init__ 里面增加了一个aa变量, 这样就不会往上查找了, 所以输出是100
print(a.x, a.y, a.aa)

print(A.aa)     # 类变量是所有实例共享的
# print(A.x)   # A 不会向下查找, 只会向上查找, 所以会报错