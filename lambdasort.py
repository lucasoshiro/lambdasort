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

#list constants
LAMBDA_EMPTY = LAMBDA_FALSE
LAMBDA_ISEMPTY = lambda l: l(lambda h: lambda t: lambda d: LAMBDA_FALSE)(LAMBDA_TRUE)

#list operations
LAMBDA_CONCAT = (lambda r: r(r)) (lambda r: lambda l1: LAMBDA_IF(LAMBDA_ISEMPTY(l1))(lambda l2: l2)((lambda r: lambda l2: LAMBDA_CONS(LAMBDA_CAR(l1))(r(r)(LAMBDA_CDR(l1))(l2)))(r)))

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

#list conversion
def ll2pl(l):
    if l2b(LAMBDA_ISEMPTY(l)): return []
    return [LAMBDA_CAR(l)] + ll2pl(LAMBDA_CDR(l))

def pl2ll(l):
    if len(l) == 0: return LAMBDA_EMPTY
    return LAMBDA_CONS(l[0])(pl2ll(l[1:]))

#list iterator
def lliterator(l):
    while not l2b(LAMBDA_ISEMPTY(l)):
        yield LAMBDA_CAR(l)
        l = LAMBDA_CDR(l)

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
def quicksort_wrapper(A):
    church = pl2ll([i2l(x) for x in A])
    sorted_church = quicksort(church)
    return [l2i(x) for x in ll2pl(sorted_church)]

def quicksort(A):
    if l2b(LAMBDA_ISEMPTY(A)): return A
    if l2b(LAMBDA_ISEMPTY(LAMBDA_CDR(A))): return A

    LR = partition(A)
    L = LAMBDA_CAR(LR)
    R = LAMBDA_CDR(LR)

    p = LAMBDA_CAR(R)
    sL = quicksort(L)
    sR = quicksort(LAMBDA_CDR(R))

    return LAMBDA_CONCAT(sL)(LAMBDA_CONS(p)(sR))

def partition_wrapper(A):
    B = pl2ll(list(map(i2l, A)))
    LR = partition(B)
    L = LAMBDA_CAR(LR)
    R = LAMBDA_CDR(LR)
    return list(map(l2i, ll2pl(L))), list(map(l2i, ll2pl(R)))

def partition(A):
    p = LAMBDA_CAR(A)
    L, R = LAMBDA_EMPTY, LAMBDA_EMPTY

    for x in lliterator(LAMBDA_CDR(A)):
        if l2b(LAMBDA_LESS(x)(p)):
            L, R = LAMBDA_CONS(x)(L), R
        else:
            L, R = L, LAMBDA_CONS(x)(R)

    L, R = L, LAMBDA_CONS(p)(R)

    return LAMBDA_CONS(L)(R)
