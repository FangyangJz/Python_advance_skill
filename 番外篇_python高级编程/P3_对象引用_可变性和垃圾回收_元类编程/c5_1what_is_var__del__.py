# python的变量实质是一个指针
a = 1
# 1. 先生成对象
# 2. 将a贴在1上

b = [1,2,3]
c = b
print(id(b), id(c))

# == 和 is 的区别
a = [1,2,3,4] # 容器写在指针区
b = [1,2,3,4]
print(a == b)
print(a is b)

# 因为基本类型写在内存
a = 1
b = 1
print(a == b)
print(a is b)

# http://www.cnblogs.com/Liubit/p/7668476.html

# 引用语义：在python中，变量保存的是对象(值)的引用，我们称为引用语义。
# 采用这种方式，变量所需的存储空间大小一致，
# 因为变量只是保存了一个引用。也被称为对象语义和指针语义。

# 值语义：有些语言采用的不是这种方式，它们把变量的值直接保存在变量的存储区里，
# 这种方式被我们称为值语义，例如C语言，采用这种存储方式，
# 每一个变量在内存中所占的空间就要根据变量实际的大小而定，无法固定下来。

a = 1
b = a
del a  # python 中垃圾回收采用引用计数, del一次就减1, 减到0就回收

# def __del__(self):  # 可以自定义del