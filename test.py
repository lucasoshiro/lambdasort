#!/usr/bin/env python3

import unittest
from lambdasort import *
from random import randint
from functools import reduce

class TestLambdasort(unittest.TestCase):
    def test_sorting(self):
        l = [randint(0, 1000) for i in range(0, 1000)]
        control = sorted(l)
        l2 = quicksort(l)
        self.assertEqual(control, l2)

    def test_partition(self):
        lst = [3, 9, 1, 5, 0, 5, 7, 9, 0, 4]
        left, right = partition(lst)
        p = car(right)
        self.assertEqual(list(filter(lambda x: x < p, left)), left)
        self.assertEqual(list(filter(lambda x: x >= p, right)), right)
        self.assertEqual(len(left) + len(right), len(lst))
        self.assertEqual(sorted(left + right), sorted(lst))
        

if __name__ == '__main__':
    unittest.main()
