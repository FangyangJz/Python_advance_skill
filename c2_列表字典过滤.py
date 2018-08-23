# [x for x in data if x>=0]
# filter(lambda x:x>=0, data)

# {k:v for k,v in d.items() if v>90}

# {x for x in s if x%3==0}

from random import randint

list1 = [randint(-10,10) for _ in range(10)]
print(list1)
print([x for x in list1 if x>0])
filter_r = filter(lambda x:x>0, list1)
print(filter_r.__next__())
print(list(filter_r))

print('-'*50)
dict1 = {'student%d' % i : randint(50,100) for i in range(1,21)}
print(dict1)
r = {k:v for k,v in dict1.items() if v>90}
print(r)
g = filter(lambda item: item[1]>90, dict1.items())
print(list(g))

print('='*50)
set1 = {randint(0,20) for _ in range(10)}
print(set1)
r = {x for x in set1 if x%3==0}
print(r)