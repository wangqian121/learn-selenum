from calculator import *
from StartEnd import *
class TestAdd(StartEnd):
    def test_add(self):
        i=Math(5,2)
        self.assertEqual(i.add(),7)
    def test_add1(self):
        i = Math(5, 5)
        self.assertEqual(i.add(), 10)
