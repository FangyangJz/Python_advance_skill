# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/15
'''
__author__ = 'Fangyang'

# 类也是对象, type创建类的类
# 什么是元类, type就是元类, 创建类的类
# 平常并不会想下面这么写 User = type(name, (base,), {attr:value, ...})
# 而是采用下面这种方式:
#
# class MetaClass(type):
#     '''把__new__方法剥离到MetaClass这里去做'''
#     def __new__(cls, *args, **kwargs):
#           return super().__new__(cls, *args, **kwargs)
#
# class User(metaclass=MetaClass):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'user'
#
# python中类的实例化过程, 首先寻找metaclass, 通过metaclass去创建User类
# 去创建类对象, 实例


def create_class(name):
    '''动态创建类'''
    if name == 'user':

        class User:
            def __str__(self):
                return 'user'
        return User

    elif name == 'company':

        class Company:
            def __str__(self):
                return 'company'
        return Company

# 灵活的创建类, 实现上面函数的作用, 用type动态创建类
# User = type('User', (), {})  # ()中是继承的基类, 不写就是object
User = type('User', (), {'name':'user'})  #  {}里是 类属性 参数

def say(self):
    # return self
    return 'i am user, I can say'

if __name__ == '__main__':

    MyClass = create_class('user')
    my_obj = MyClass()
    print(my_obj, type(my_obj))

    my_obj2 = User()
    print(my_obj2, type(my_obj2))
    print(my_obj2.name)

    UserII = type('UserII', (), {'name': 'user', 'say':say})
    # () base类要写逗号, 比如 (BaseClass, )
    my_obj3 = UserII()
    print(my_obj3, type(my_obj2))
    print(my_obj3.say())