from c2_7静态方法_类方法以及对象方法和参数 import Date

class User:
    def __init__(self, birthday):
        self.__birthday = birthday   # 这里加了双下划线变成私有属性, 我们就不能用.__birthday去访问了

    def get_age(self): # 只有 类里的方法 可以访问私有属性
        return 2018 - self.__birthday.year 

class Student(User):
    def __init__(self, birthday):
    # Python3.x 和 Python2.x 的一个区别是: 
    # Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx :
    # super类功能：新式类实现广度优先的不重复的调用父类，解决了钻石继承（多继承）的难题
        super().__init__(birthday)  # 调用父类中的 __init__()方法


if __name__ == "__main__":
    user = User(Date(1990,2,1))
    # print(user.birthday)
    print(user.get_age())
    print(user._User__birthday)   # 通过这种方法可以访问到私有属性, 但是不推荐