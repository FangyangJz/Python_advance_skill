# 切片模式 [start:end:stop]
aList = [3,4,5,6,1,2,3]
print(aList[::])  # 返回包含原列表中的所有元素的一个新列表
print(aList[::-1])  # 返回包含原列表中的所有元素的一个新逆序列表
print(aList[0:100])  # 超出列表范围的, 自动截取列表尾部 
print(aList[100:])  # 切片位置起始位置大于列表长度, 返回空列表

aList[len(aList):] = [9]   # 在列表尾部增加元素
print(aList) 

aList[:0] = [1, 2]   # 在列表头部增加元素, 这么写可能不是太好理解
print(aList)        # 相当于 [1,2] + aList 

aList[3:3] = [4000]  # 在列表中间位置插入元素
print(aList)

aList[::2] = [0]*6  # 隔一个修改一个, 长度要符合列表长度, [0]*6 相当于 [0,0,0,0,0,0]
print(aList)

aList[:3] = []  # 相当于删除元素
print(aList)

del aList[::3]  # 隔2个删一个
print(aList)