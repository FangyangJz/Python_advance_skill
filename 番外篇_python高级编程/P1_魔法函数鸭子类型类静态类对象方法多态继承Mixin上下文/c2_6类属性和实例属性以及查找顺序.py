# class A:
#     name = "A"
#     def __init__(self):
#         self.name = "obj"

# a = A()
# print(a.name)

# C3算法, 新式类
# MRO method resolve order
class D:
    pass

class C(D):
    pass

class B(D):
    pass

class A(B, C):
    pass

print(A.__mro__)
# (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)