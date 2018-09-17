import unittest
from c0_count import Count

class TestCount(unittest.TestCase):
    def setUp(self):
        print('setup')
        self.obj = Count()
    
    def tearDown(self):
        print('teardown')
        self.obj = None
    
    def add_test(self):
        print(self.obj.add(10,20)==30)
    
    def sub_test(self):
        print(self.obj.sub(10,2)==8)

def get_suite():
    demo_countadd = TestCount('add_test')
    demo_countsub = TestCount('sub_test')

    case_list = ['add_test', 'sub_test']
    demos = map(TestCount, case_list)
    suite1 = unittest.TestSuite()
    suite1.addTests(demos)
    return suite1

    # suite0 = unittest.TestSuite()
    # suite0.addTest(demo_countadd)
    # suite0.addTest(demo_countsub)
    # return suite0


class countTestSuite(unittest.TestSuite):
    def __init__(self):
        case_list = ['add_test', 'sub_test']
        super().__init__(map(TestCount, case_list))


if __name__ == '__main__':
    # s = get_suite()
    s = countTestSuite()  # 用类的这种方法代替上面那种, 使代码更加简洁
    print(s.countTestCases()) 
    runner = unittest.TextTestRunner()
    runner.run(s)