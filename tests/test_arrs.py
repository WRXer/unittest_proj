import unittest
from utils import arrs


class TestArrs(unittest.TestCase):
    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)


    def test_get_2(self):
        self.assertEqual(arrs.get([], -1, "test"), "test")


    def test_slice_1(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])


    def test_slice_2(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], -1), [3])


    def test_slice_3(self):
        self.assertEqual(arrs.my_slice([]), [])


    def test_slice_4(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], -4, 3), [1, 2, 3])