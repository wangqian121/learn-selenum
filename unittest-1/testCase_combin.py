from calculator import *
import unittest
class Test_StartEnd(unittest.TestCase):
    def setUp(self):
        print('start')
    def tearDown(self):
        print('end')
class Testadd(Test_StartEnd):
    def test_add(self):
        j=Math(5,2)
        self.assertEqual(j.add(),7)

class Testsub(Test_StartEnd):
    def test_sub(self):
        i=Math(3,2)
        self.assertEqual(i.sub(),1)

if __name__ == '__main__':
    unittest.main()