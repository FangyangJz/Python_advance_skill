# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
# 程序源代码：

import time

D=input("请输入年份，格式如XXXX-XX-XX：")
d=time.strptime( D,'%Y-%m-%d').tm_yday
print ("the {} day of this year!".format(d))