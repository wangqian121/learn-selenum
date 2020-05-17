import unittest
class StartEnd(unittest.TestCase):
    def setUp(self):
        print('start')
    def tearDown(self):
        print('end')
