#!/usr/bin/env python3

import unittest
from lambdasort import *
from random import randint
from functools import reduce

l = [37, 3, 15, 17, 18, 18, 1, 33, 28, 39, 34, 37, 12, 1, 13, 30, 13, 10, 32,
     34, 4, 34, 3, 46, 49, 8, 9, 29, 29, 30, 36, 28, 40, 38, 33, 26, 30, 2, 43,
     46, 46, 47, 32, 26, 30, 36, 13, 44, 26, 42]

class TestLambdasort(unittest.TestCase):
    def test_sorting(self):
        control = sorted(l)
        l2 = quicksort(l)
        self.assertEqual(control, l2)

    def test_partition(self):
        lst = [3, 9, 1, 5, 0, 5, 7, 9, 0, 4]
        left, right = partition_wrapper(lst)
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

    def test_l2i(self):
        self.assertEqual(l2i(LAMBDA_ZERO), 0)
        self.assertEqual(l2i(LAMBDA_ONE), 1)
        self.assertEqual(l2i(LAMBDA_TWO), 2)

    def test_i2l(self):
        n = 42
        self.assertEqual(l2i(i2l(n)), n)

    def test_LAMBDA_INCREMENT(self):
        self.assertEqual(l2i(LAMBDA_INCREMENT(LAMBDA_TWO)), 3)

    def test_LAMBDA_DECREMENT(self):
        self.assertEqual(l2i(LAMBDA_DECREMENT(LAMBDA_TWO)), 1)

    def test_LAMBDA_ADD(self):
        self.assertEqual(l2i(LAMBDA_ADD(i2l(20))(i2l(15))), 35)

    def test_LAMBDA_SUB(self):
        self.assertEqual(l2i(LAMBDA_SUB(i2l(20))(i2l(15))), 5)

    def test_LAMBDA_EQZ(self):
        self.assertTrue(l2b(LAMBDA_EQZ(i2l(0))))
        self.assertFalse(l2b(LAMBDA_EQZ(i2l(1))))

    def test_LAMBDA_LEQ(self):
        self.assertTrue(l2b(LAMBDA_LEQ(i2l(10))(i2l(10))))
        self.assertTrue(l2b(LAMBDA_LEQ(i2l(10))(i2l(42))))
        self.assertFalse(l2b(LAMBDA_LEQ(i2l(42))(i2l(10))))

    def test_LAMBDA_EQ(self):
        self.assertTrue(l2b(LAMBDA_EQ(LAMBDA_ONE)(LAMBDA_ONE)))
        self.assertFalse(l2b(LAMBDA_EQ(LAMBDA_ONE)(LAMBDA_ZERO)))
        self.assertFalse(l2b(LAMBDA_EQ(LAMBDA_ONE)(LAMBDA_TWO)))

    def test_LAMBDA_LESS(self):
        self.assertFalse(l2b(LAMBDA_LESS(i2l(10))(i2l(10))))
        self.assertTrue(l2b(LAMBDA_LESS(i2l(10))(i2l(42))))
        self.assertFalse(l2b(LAMBDA_LESS(i2l(42))(i2l(10))))

    def test_llist2pylist(self):
        self.assertEqual(llist2pylist([LAMBDA_ZERO, LAMBDA_ONE, LAMBDA_TWO]),
                         [0, 1, 2])

    def test_pylist2llist(self):
        self.assertEqual(llist2pylist(pylist2llist([0, 1, 2])), [0, 1, 2])

if __name__ == '__main__':
    unittest.main()
