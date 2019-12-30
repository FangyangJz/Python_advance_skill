# unittest.makeSuite 自动构建测试集
# 1. 测试方法都以规定的命名开头
# 2. 使用makeSuite直接生产测试集

# 还有一种最简单的方式: unittest.main()
# 自动检测测试类中所有以test开头的方法:
# 1. 自动查找测试用例
# 2. 自动构建测试集
# 3. 自动运行测试用例

import unittest
from c0_count import Count

class TestCount(unittest.TestCase):
    def setUp(self):
        print('setup')
        self.obj = Count()
    
    def tearDown(self):
        print('teardown')
        self.obj = None
    
    def test_add(self):
        print(self.obj.add(10,20)==30)
    
    def test_sub(self):
        print(self.obj.sub(10,2)==8)

def get_suite():
    suite = unittest.makeSuite(TestCount, prefix='test')
    print(suite.countTestCases())
    return suite


if __name__ == '__main__':
    # s = get_suite()
    # runner = unittest.TextTestRunner()
    # runner.run(s)

    unittest.main()