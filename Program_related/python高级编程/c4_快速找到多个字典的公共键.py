from random import randint, sample

# 随机生成key为球员名字, value为进球个数
t1 = {k:randint(1,4) for k in sample('abcdefg',randint(3,6))}
t2 = {k:randint(1,4) for k in sample('abcdefg',randint(3,6))}
t3 = {k:randint(1,4) for k in sample('abcdefg',randint(3,6))}
print(t1, t2, t3, sep='\n')
r = t1.keys() & t2.keys()
print(r)

print('-'*50)
from functools import reduce
fibb = reduce(lambda a,b : a+b, range(1,11))
print(fibb)
t_list = [t1, t2, t3]
print(t_list)
get_keys = list(map(dict.keys, t_list))
print(get_keys)
common_key = reduce(lambda a,b: a&b, get_keys)
print(common_key)