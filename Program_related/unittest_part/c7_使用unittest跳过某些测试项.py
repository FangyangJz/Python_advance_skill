# 自动化测试问题
# 1. 跳过测试用例给出具体原因;
# 2. 依赖于某种条件测试;
# 3. 测试结果不计入测试统计;

# 1. 忽略测试用例
# skip(reson) # 实质:装饰器
# 例子: 
# @unittest.skip('Not Test')
# def add(x, y):
#     pass

# 2. 根据条件跳过测试用例
# skipIf(condition, reason)   # 如果条件为真, 就跳过
# skipUnless(condition, reason)  # 和skipIf相反, 条件为真,才不跳过, 执行
# 例如:
# @unittest.skipIf(Count.Version > 1, 'Low version')
# def add(x, y):
#     pass

# 3. 预期结果失败
# expectedFailure(func)
# 例子:
# @unittest.expectedFailure
# def add(x, y):
#     return x+y
# 测试结果与预期值不同, 不计入失败统计


import unittest
from c0_count import Count

class TestCount(unittest.TestCase):
    def setUp(self):
        print('setup')
        self.obj = Count()
    
    def tearDown(self):
        print('teardown')
        self.obj = None
    
    # @unittest.skip('Not test')
    def test_add(self):
        # print(self.obj.add(10,20)==30)
        self.assertEqual(self.obj.add(10,20), 30)
    
    @unittest.skipIf(Count.version==1, 'low version skip')
    # @unittest.expectedFailure
    def test_sub0(self):
        print(self.obj.sub(10,2)==8)
        self.assertEqual(self.obj.sub(10,2), 8)

    @unittest.expectedFailure
    def test_sub1(self):
        print(self.obj.sub(10,2)==8)
        self.assertEqual(self.obj.sub(10,2), 6)


if __name__ == '__main__':
    unittest.main()