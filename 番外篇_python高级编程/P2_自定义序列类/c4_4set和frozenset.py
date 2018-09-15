# set 集合 , frozenset(不可变集合), 无序, 不重复
# - & | 
# set的效率很高, 推荐使用
# 有__contain__(), 所以可以用in判断
# 判断是否是子集, .issubset()

s = 'abc'

ss = set(s)  # 有add方法
fs = frozenset(s) # 没有add, update方法, 可以作为dict的key
ss.update({'aa','bb'})
print(ss)
print(fs)

re_set = ss.difference(set('bcd'))  # 注意是ss的差集相当于 -(魔法函数__isub__), 不是补集
print(re_set)
