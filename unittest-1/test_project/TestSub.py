from calculator import *
from StartEnd import *
class TestSub(StartEnd):
    def test_sub(self):
        i=Math(5,2)
        self.assertEqual(i,sub(),3)
    def test_sub1(self):
        i=Math(8,5)
        self.assertEqual(i.sub(),3)
