
import numbers    # python内置包, 预置了python中的很多数据类型


class Group(object):

    # 支持切片操作

    # 通过c3_1例子, 看abc里面的Sequence类
    # 题外话  在类方法(注意不是对象方法, 不用def 声明定义)使用
    #  __slots__ = ('attr1', 'attr2')     仅允许动态绑定()类里面有的属性,
    # 可以减少所有实例属性消耗的内存, 提升性能40%-50%

    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()

    def __getitem__(self, item):
        # return self.staffs[item]
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False


staffs = ['b1', 'b2', 'b3']
group = Group(company_name='imooc', group_name='user', staffs=staffs)
sub_group = group[:2]  # 如果注释掉 __getitem__(self, item): 方法, 这句会报错
print(list(sub_group))
print(len(group))

if 'b1' in group:
    print('yes')

for user in group:
    print(user)

reversed(group)
for user in group:
    print(user)