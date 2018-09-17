
class Company(object):
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs

    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)


def add(a, b):
    a += b
    return a

if __name__=='__main__':
    a = 1
    b = 2
    print(add(a, b))
    print(a, b)

    a = (1, 2)
    b = (3, 4)
    print(add(a, b))
    print(a, b)

    a = [1, 2]
    b = [3, 4]
    print(add(a, b))  # 这里暴露了问题
    print(a, b)

    print('-'*50)
####################
    com1 = Company('com1', ['b1', 'b2'])
    com1.add('b3')
    com1.remove('b1')
    print(com1.staffs)
    print('-' * 50)

    com2 = Company('com2')
    com2.add('b')
    print(com2.staffs)
    print(com2.__init__.__defaults__)  # 没传参, 用默认值, 就会在这里,
    # 所以不传参用 可变序列 容器一定要注意, 这也解释了上面为什么用tuple传参没问题
    # 传入的参数 用 可变序列 要注意这个问题
    print('=' * 50)

    com3 = Company('com3')  # 问题是 com2 和 com3 共用了同一个 []
    print(com3.__init__.__defaults__)
    com3.add('b5')

    print(com2.staffs)
    print(com3.staffs)
    print(com2.staffs is com3.staffs)

    print(com2.__init__.__defaults__)