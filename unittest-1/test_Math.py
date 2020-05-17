from calculator import *
import unittest

class Test_add(unittest.TestCase):
    def setUp(self):
        print("start test")
    # def test_add(self):
    #     j=Math(5,10)
    #     self.assertEqual(j.add(),15)
    # def test_add1(self):
    #     j=Math(5,10)
    #     self.assertNotEqual(j.add(),10)

    def test_addertIs(self):
        self.assertIs('ww','ww')
    def tearDown(self):
        print("test end")
class Test_sub(unittest.TestCase):
    def setUp(self):
        print("start2")
    def test_sub(self):
        a=Math(10,2)
        self.assertEqual(a.sub(),8)
    def tearDown(self):
        print("end")

if __name__=='__main__':
    #构造测试集
    suite=unittest.TestSuite()
    suite.addTest(Test_add("test_addertIs"))
    suite.addTest(Test_sub("test_sub"))

    #执行测试
    runner=unittest.TextTestRunner()
    runner.run(suite)

