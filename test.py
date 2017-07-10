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

    def test_l2b(self):
        self.assertEqual(l2b(LAMBDA_TRUE), True)
        self.assertEqual(l2b(LAMBDA_FALSE), False)

    def test_b2l(self):
        self.assertEqual(l2b(b2l(True)), True)
        self.assertEqual(l2b(b2l(False)), False)

    def test_LAMBDA_OR(self):
        self.assertTrue(l2b(LAMBDA_OR(b2l(False))(b2l(True))))
        self.assertTrue(l2b(LAMBDA_OR(b2l(True))(b2l(False))))
        self.assertTrue(l2b(LAMBDA_OR(b2l(True))(b2l(True))))
        self.assertFalse(l2b(LAMBDA_OR(b2l(False))(b2l(False))))
        
    def test_LAMBDA_AND(self):
        self.assertFalse(l2b(LAMBDA_AND(b2l(False))(b2l(True))))
        self.assertFalse(l2b(LAMBDA_AND(b2l(True))(b2l(False))))
        self.assertTrue(l2b(LAMBDA_AND(b2l(True))(b2l(True))))
        self.assertFalse(l2b(LAMBDA_AND(b2l(False))(b2l(False))))

    def test_LAMBDA_NOT(self):
        self.assertFalse(l2b(LAMBDA_NOT(b2l(True))))
        self.assertTrue(l2b(LAMBDA_NOT(b2l(False))))

    def test_LAMBDA_IF(self):
        self.assertTrue(l2b(LAMBDA_IF(b2l(True))(LAMBDA_TRUE)(LAMBDA_FALSE)))
        self.assertFalse(l2b(LAMBDA_IF(b2l(False))(LAMBDA_TRUE)(LAMBDA_FALSE)))

if __name__ == '__main__':
    unittest.main()
