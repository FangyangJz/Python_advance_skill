s = 'ab;df|erew|sdf,jk|mn\sdf;rst,uwv\dfs/sef'

from functools import reduce
import re

# 这种方法就是让你熟悉下函数式编程的这几个函数
# 现实中这么写code是要被人打死的
r = reduce(lambda l, sep: sum(map(lambda ss: ss.split(sep), l), []), ',;|\/', [s])
print(r)

# 正常应该用正则表达式 re.split()
r = re.split('[\\;,/|]', s)
print(r)

