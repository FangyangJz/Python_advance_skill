# 自省是通过一定的机制查询到对象的内部结构

class Person:
    '''文档1233333333'''
    name = 'user'


class Student(Person):
    
    name_student = 'stu'

    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == "__main__":
    user = Student("JJJJ")

    # instance中通过__dict__查询属性, 只会查到属于这个实例的属性字典,
    # 继承过来的 类的属性, 或者本身类的属性, 都不会被 __dict__ 查询到
    # 题外话, 在python中__dict__是一种效率特别高的数据结构, 底层用C写的
    print(user.__dict__)
    print(user.name)
    print(Person.__dict__)
    print(Student.__dict__)

    # 除了 __dict__ 查询外, 实例的__dict__也可赋值
    user.__dict__['school_addr'] = '大庆市aaa'
    print(user.school_addr)

    # dir(实例) 能列 对象 更加详细的信息
    print(dir(user))

    # .__dict__ 只能看实例, dir能看任何对象
    print('-'*50)
    a = [1,2,3]
    print(dir(a), len(dir(a)))
    print('-'*50)
    print(a.__dir__(), len(a.__dir__()))  # 再次证明了magic函数
    print('-'*50)
    print(a.__dict__)