
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list
    
    def __getitem__(self, item):
        '''
        类里面有了这个魔法函数, 那么它生成的对象是可迭代的
        注意! 这个方法遇到异常才能结束, 这里是有限的数据迭代完抛出异常,停止
        '''
        return self.employee[item]

# 实现了迭代
company = Company(['tom', 'bobo', 'jam'])
for em in company:
    print(em)

# 还可以实现切片
company1 = Company(['a', 'b', 'c', 'd'])
company1 = company1[2:4]
print(len(company1))
for em in company1:
    print(em)