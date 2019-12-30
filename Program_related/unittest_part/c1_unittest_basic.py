# 测试用例编写的基本结构
# class TestCase(unittest.TestCase):
#     def setUp(self): # 初始化
#     def runTest(self):  # 测试
#     def tearDown(self):  # 回复现场
# unittest.main()

import unittest
from c0_count import add, sub, div
# print(dir(unittest))

class TestAdd(unittest.TestCase):
    
    def setUp(self):
        print('call setUp')
    
    def runTest(self):
        print('runTest')
        print(add(10,20)==30)

    def tearDown(self):
        print('call tearDown')


class TestSub(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def runTest(self):
        # print('runTest')
        print(sub(10,5)==5)

    def tearDown(self):
        pass

def main():
    demo_add = TestAdd()
    demo_sub = TestSub()
    demo_add.run()
    demo_sub.run()

if __name__ == '__main__':
    main()