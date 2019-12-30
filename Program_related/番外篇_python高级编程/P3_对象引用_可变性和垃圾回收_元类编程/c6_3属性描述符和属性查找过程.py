# 属性描述符, 可以用来做 属性类型 检查
# 只要定义一个类, 实现了__get__或__set__或__delete__任意一个魔法函数,
# 那么他就是一个 属性描述符


# 如果user是某个类的实例, 那么user.age(以及等价的getattr(user, 'age'))
# 首先调用__getattribute__, 如果类定义了__getattr__方法,
# 那么在__getattribute__抛出 AttributeError 的时候就会调用__getattr__,
# 而对于描述符(__get__)的调用, 则是发生在 __getattribute__ 内部的

# user = User(), 那么user.age顺序如下:
# 1. 如果age出现在User或其基类的__dict__中, 且age是data desciptor, 那么调用其__get__, 否则
#     (先去查查类)

# 2. 如果age出现在user实例的__dict__中, 那么直接返回user.__dict__['age'], 否则
#     (再去查实例)

# 3. 如果age出现在User或其基类的__dict__中
#     3.1 如果age是non-data discriptor, 那么调用其__get__方法, 否则
#     3.2 返回 __dict__['age']

# 4. 如果User有__getattr__方法, 调用__getattr__方法, 否则
# 5. 抛出AttributerError异常

# 参考阅读 https://www.cnblogs.com/Jimmy1988/p/6808237.html

import numbers

class IntField:
    def __get__(self, instance, owner):
        return self.value  # 将下面保存的value返回

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('int value need')
        self.value = value  # 把合格的value保存在 IntField 的实例内

        if value < 0:
            raise ValueError('positive value need')  # 当然还可以增加更多判断, 检查属性的赋值

    def __delete__(self, instance):
        pass


class NonDataIntFild:
    # 非数据描述符
    # 问题4. 什么是数据描述符，什么是非数据描述符？
　  #　答：一个类，如果只定义了 __get__() 方法，而没有定义 __set__(), __delete__() 方法，则认为是非数据描述符； 反之，则成为数据描述符
    def __get__(self, instance, owner):
        return self.value


class User:
    # age = IntField()
    age2 = NonDataIntFild()


if __name__ == '__main__':
    user = User()
    # user.age = 30
    # print(user.__dict__)
    # # print(user.age)   # 和下面这句等价
    # print(getattr(user, 'age'))

    # user.age = 'aaa'
    # print(user.age)

    user.age2 = 100
    print(user.__dict__)
    # print(user.age)   # 和下面这句等价
    print(getattr(user, 'age2'))
