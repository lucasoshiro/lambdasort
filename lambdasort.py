#!/usr/bin/env python3

def car(A):
    return A[0]

def cdr(A):
    return A[1:]

def cons(A, x):
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
        if x < p: L = cons(L, x)
        else: R = cons(R, x)

    R = cons(R, p)

    return L, R
