# 实际编程过程中 不推荐多继承
# 1. MRO算法容易导致预料不到的问题
# 2. 容易造成继承关系的混乱

# 解决上面的问题, 用 Mixin 混合模式 啊
# mixin的特点:
# 1. Mixin类功能单一
# 2. 不和基类关联, 可以和任意基类组合, 基类可以不和mixin关联就能初始化成功
# 3. 在mixin中不要使用 super 这种用法

# 不成文的规则, mixin尽量以Mixin结尾

class Function1Mixin(object):
    def func1(self, *args, **kwargs):
        print("我是功能1")
        return 1

class Function2Mixin(object):
    def func2(self, *args, **kwargs):
        print("我是功能2")
        return 2

class RealClass(object):
    print('我是真的基类aaaa')

class New(Function1Mixin, Function2Mixin, RealClass):
    print('我是继承了func1, func2 的New类')


if __name__ == "__main__":
    n = New()
    n.func1()
    n.func2()