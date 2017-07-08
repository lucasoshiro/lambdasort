#!/usr/bin/env python3

import unittest
from lambdasort import *
from random import randint

class TestLambdasort(unittest.TestCase):
    def test_sorting(self):
        l = [randint(0, 40) for i in range(0, 40)]
        control = sorted(l)
        l2 = quicksort_wrapper(l)
        self.assertEqual(control, l2)

if __name__ == '__main__':
    unittest.main()
