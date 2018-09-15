# 和容器相关的抽象基类都是放在abc里面的
from collections import abc

a = [1,2]
c = a + [3,4]
print(c)

a += [3,4]
print(a)

print('-'*50)
a += (3,4)   # += 这里 可以是元组, 可以是任意序列类型
# += 实际上是去调用的 collections.abc 里面的 MutableSequence的 __iadd__(self, values)
# 那个iadd方法里面是self.extend(values) 然后 return self
# def extend(self, iterable) 方法实际上是 
#       for v in iterable:
#            self.append(v)
#  没有返回值
print(a)

# a = [1,2]
# c = a + (3,4) # + 号这里 不能是元组
# print(c)