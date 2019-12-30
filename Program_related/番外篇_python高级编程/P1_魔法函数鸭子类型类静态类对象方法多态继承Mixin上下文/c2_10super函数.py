class A:
    
    aa = 'aa'
    print("A class function")

    def __init__(self):
        self.a = 'a'
        print('A')


class B(A):
    def __init__(self):
        print('B')
        # python2 写法
        # super(B, self).__init__()
        # python3 写法
        super().__init__()  # 如果不写这句, 那么就不去执行父类中__init__()构造函数
        # super() 的好处是可以重用代码!!!


if __name__ == "__main__":
    b = B()
    print(b.aa)  # 因为aa是类中的属性, 所以只要继承, 无需super就能访问