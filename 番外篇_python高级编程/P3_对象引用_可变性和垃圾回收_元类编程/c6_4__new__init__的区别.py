
class User:
    def __new__(cls, *args, **kwargs):  # 新式类, python2没有
    # 允许我们在生成 实例对象 前生成类干的事情, 比__init__早啊
    # new用来控制对象的生成过程, 在对象生成之前
    # 如果new里面不返还对象, 则不会调用init函数
    # new在后面元类编程会详细介绍, 高级框架中用的多, 一般不需要重写
        print('in new')
        return super().__new__(cls)   # 通过这句去调用init

    def __init__(self, name):
    # init 是用来完善对象实例的
        print('in init')
        self.name = name

if __name__ == '__main__':
    user = User('haha')
    print(user.name)
