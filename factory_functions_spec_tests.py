import unittest
from bread_factory import *

class TestFactoryFunctions(unittest.TestCase):
    # test 1
    def test_make_dough(self):
        self.assertEqual(make_dough('water','flour'),'dough')
        self.assertEqual(make_dough('water','oats'),'not dough')
        self.assertEqual(make_dough('water','wholegrain flour'),'brown dough')

    def test_make_bread(self):
        self.assertEqual(make_bread('dough'), 'bread')
        self.assertEqual(make_bread('not dough'), 'not bread')
        self.assertEqual(make_bread('brown dough'), 'brown bread')

if __name__ == '__main__':
    unittest.main()


