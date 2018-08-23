# 1. 定义一系列数值常量或枚举类型
# 2. 使用 collections.namedtuple 替代内置tuple

NAME, AGE, SEX, EMAIL = range(4)
s = ('jim', 16, 'male', 'jim@123.com')
print(s[NAME])

from enum import IntEnum

class StudentEnum(IntEnum):
    NAME = 0
    AGE = 1
    SEX = 2
    EMAIL = 3

print(s[StudentEnum.NAME])

######################################
from collections import namedtuple
Student = namedtuple('student', ['name', 'age', 'sex', 'email'])
s2 = Student(*s)
print(s2)
print(isinstance(s2, tuple))
print(s2.name)