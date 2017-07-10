#!/usr/bin/env python3

LAMBDA_TRUE = lambda a, b: a
LAMBDA_FALSE = lambda a, b: b

def l2b(l):
    return l(True, False)

def b2l(b):
    return LAMBDA_TRUE if b else LAMBDA_FALSE

def car(A):
    return A[0]

def cdr(A):
    return A[1:]

def insert(A, x):
    return [x] + A

def concat(A, B):
    return A + B

def quicksort(A):
    if len(A) <= 1: return A
    L, R = partition(A)
    p = car(R)
    L = quicksort(L)
    R = quicksort(cdr(R))
    return concat(L, concat([p], R))

def partition(A):
    p = car(A)
    L = []
    R = []

    for x in cdr(A):
        if x < p: L = insert(L, x)
        else: R = insert(R, x)

    R = insert(R, p)

    return L, R
