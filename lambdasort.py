#!/usr/bin/env python3


#boolean constants
LAMBDA_TRUE = lambda a: lambda b: a
LAMBDA_FALSE = lambda a: lambda b: b

#boolean opearations
LAMBDA_OR = lambda a: lambda b: a(LAMBDA_TRUE)(b)
LAMBDA_AND = lambda a: lambda b: a(b)(LAMBDA_FALSE)
LAMBDA_NOT = lambda a: a(LAMBDA_FALSE)(LAMBDA_TRUE)

#if
LAMBDA_IF = lambda c: lambda t: lambda e: c(t)(e)

#integer constants
LAMBDA_ZERO = lambda p: lambda x: x
LAMBDA_ONE = lambda p: lambda x: p(x)
LAMBDA_TWO = lambda p: lambda x: p(p(x))

#integer operations
LAMBDA_INCREMENT = lambda l: lambda p: lambda x: p(l(p)(x))
LAMBDA_DECREMENT = lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda y: x)(lambda y: y)
LAMBDA_ADD = lambda m: lambda n: n(LAMBDA_INCREMENT)(m)
LAMBDA_SUB = lambda m: lambda n: n(LAMBDA_DECREMENT)(m)

#comparators
LAMBDA_EQZ = lambda n: n(lambda x: LAMBDA_FALSE)(LAMBDA_TRUE)
LAMBDA_LEQ = lambda m: lambda n: LAMBDA_EQZ(LAMBDA_SUB(m)(n))
LAMBDA_EQ = lambda m: lambda n: LAMBDA_AND(LAMBDA_LEQ(m)(n))(LAMBDA_LEQ(n)(m))
LAMBDA_LESS = lambda m: lambda n: LAMBDA_AND(LAMBDA_LEQ(m)(n))(LAMBDA_NOT(LAMBDA_EQ(m)(n)))

#pair operations
LAMBDA_CONS = lambda a: lambda b: lambda l: l(a)(b)
LAMBDA_CAR = lambda p: p(lambda a: lambda b: a)
LAMBDA_CDR = lambda p: p(lambda a: lambda b: b)

#boolean conversion
def l2b(l):
    return l(True)(False)

def b2l(b):
    return LAMBDA_TRUE if b else LAMBDA_FALSE

#integer conversion
def l2i(l):
    return l(lambda x: x + 1)(0)

def i2l(i):
    l = LAMBDA_ZERO
    for j in range(0, i):
        l = LAMBDA_INCREMENT(l)

    return l

def llist2pylist(L):
    return list(map(l2i, L))

def pylist2llist(L):
    return list(map(i2l, L))

#pair conversion
def l2p(l):
    return [LAMBDA_CAR(l), LAMBDA_CDR(l)]

def p2l(p):
    return LAMBDA_CONS(p[0])(p[1])

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
    L, R = partition_wrapper(A)
    p = car(R)
    L = quicksort(L)
    R = quicksort(cdr(R))
    return concat(L, concat([p], R))

def partition_wrapper(A):
    B = pylist2llist(A)
    L, R = partition(B)
    return llist2pylist(L), llist2pylist(R)

def partition(A):
    p = car(A)

    L, R = [], []

    for x in cdr(A):
        if l2b(LAMBDA_LESS(x)(p)):
            L, R = cons(x, L), R
        else:
            L, R = L, cons(x, R)

    L, R = L, cons(p, R)

    return L, R
