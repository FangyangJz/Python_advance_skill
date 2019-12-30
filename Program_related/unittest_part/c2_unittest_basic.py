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

if __name__ == '__main__':
    demo_count = TestCount('add_test')
    demo_count.run()
    demo_count = TestCount('sub_test')
    demo_count.run()