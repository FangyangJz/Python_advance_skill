import unittest

# main.py流程
# main = TestProgram
# createTests()  ->  loadTestsFrom<odule(loader.py : TestLoader)  -> suiteClasses(suite.py : testSuite)
# runTest()  ->  run() (runner.py : TextTestRunner)

# TestCase测试用例测试流程:
# for case in Cases -> setUp -> run_case -> tearDown

