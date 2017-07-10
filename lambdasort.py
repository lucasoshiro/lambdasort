#!/usr/bin/env python3

#boolean constants
LAMBDA_TRUE = lambda a, b: a
LAMBDA_FALSE = lambda a, b: b

#boolean opearations
LAMBDA_OR = lambda a, b: a(LAMBDA_TRUE, b)
LAMBDA_AND = lambda a, b: a(b, LAMBDA_FALSE)
LAMBDA_NOT = lambda a: a(LAMBDA_FALSE, LAMBDA_TRUE)

#boolean conversion
def l2b(l):
    return l(True, False)

def b2l(b):
    return LAMBDA_TRUE if b else LAMBDA_FALSE

#list operators
def car(A):
    return A[0]

def cdr(A):
    return A[1:]

def insert(A, x):
    return [x] + A

def concat(A, B):
    return A + B

#quicksort
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
