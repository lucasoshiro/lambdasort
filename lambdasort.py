#!/usr/bin/env python3

LAMBDA_TRUE = lambda a: lambda b: a
LAMBDA_FALSE = lambda a: lambda b: b

#boolean opearations
LAMBDA_OR = lambda a: lambda b: a(LAMBDA_TRUE)(b)
LAMBDA_AND = lambda a: lambda b: a(b)(LAMBDA_FALSE)
LAMBDA_NOT = lambda a: a(LAMBDA_FALSE)(LAMBDA_TRUE)

#if
LAMBDA_IF = lambda c: lambda t: lambda e: c(t)(e)

#boolean conversion
def l2b(l):
    return l(True)(False)

def b2l(b):
    return LAMBDA_TRUE if b else LAMBDA_FALSE

#list operators
def car(A):
    return A[0]

def cdr(A):
    return A[1:]

def cons(x, A):
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

    L, R = [], []

    for x in cdr(A):
        if x < p:
            L, R = cons(x, L), R
        else:
            L, R = L, cons(x, R)

    L, R = L, cons(p, R)

    return L, R
