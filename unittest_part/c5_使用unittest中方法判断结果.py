import unittest

# unittest.TestCase.
# assertNotEqual(a,b)   a!=b
# assertEqual(a,b)  a==b
# assertTrue(x)    x is True
# assertFalse(x)   x is False
# assertIs(a,b)    a is b
# assertIsNot(a,b)  a not b
# assertIsNone(x)   x is None

from c0_count import Count

class TestCount(unittest.TestCase):
    def setUp(self):
        print('setup')
        self.obj = Count()
    
    def tearDown(self):
        print('teardown')
        self.obj = None
    
    def test_add(self):
        # print(self.obj.add(10,20)==30)
        self.assertEqual(self.obj.add(10,20), 30)
    
    def test_sub(self):
        print(self.obj.sub(10,2)==8)
        self.assertEqual(self.obj.sub(10,2), 8)


if __name__ == '__main__':
    unittest.main()