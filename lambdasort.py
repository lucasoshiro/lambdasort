#!/usr/bin/env python3

from consts import *

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

#quicksort
def quicksort_wrapper(A):
    church = pl2ll([i2l(x) for x in A])
    sorted_church = quicksort(church)
    return [l2i(x) for x in ll2pl(sorted_church)]

def partition_wrapper(A):
    B = pl2ll(list(map(i2l, A)))
    LR = partition(B)
    L = LAMBDA_CAR(LR)
    R = LAMBDA_CDR(LR)
    return list(map(l2i, ll2pl(L))), list(map(l2i, ll2pl(R)))

_partition2 = lambda x: lambda L: lambda R: lambda p: (lambda c: lambda t: lambda e: c(t)(e))((lambda m: lambda n: (lambda a: lambda b: a(b)((lambda a: lambda b: b)))((lambda m: lambda n: (lambda n: n(lambda x: (lambda a: lambda b: b))((lambda a: lambda b: a)))((lambda m: lambda n: n((lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda y: x)(lambda y: y)))(m))(m)(n)))(m)(n))((lambda a: a((lambda a: lambda b: b))((lambda a: lambda b: a)))((lambda m: lambda n: (lambda a: lambda b: a(b)((lambda a: lambda b: b)))((lambda m: lambda n: (lambda n: n(lambda x: (lambda a: lambda b: b))((lambda a: lambda b: a)))((lambda m: lambda n: n((lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda y: x)(lambda y: y)))(m))(m)(n)))(m)(n))((lambda m: lambda n: (lambda n: n(lambda x: (lambda a: lambda b: b))((lambda a: lambda b: a)))((lambda m: lambda n: n((lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda y: x)(lambda y: y)))(m))(m)(n)))(n)(m)))(m)(n))))(x)(p))((lambda a: lambda b: lambda l: l(a)(b))((lambda a: lambda b: lambda l: l(a)(b))(x)(L))(R))((lambda a: lambda b: lambda l: l(a)(b))(L)((lambda a: lambda b: lambda l: l(a)(b))(x)(R)))

_partition3 = lambda r: lambda S: lambda LR: lambda p: r(r)((lambda p: p(lambda a: lambda b: b))(S))((lambda p: p(lambda a: lambda b: a))(LR))((lambda p: p(lambda a: lambda b: b))(LR))(p)

_partition = (lambda r: r(r))(lambda r: lambda S: (lambda c: lambda t: lambda e: c(t)(e))((lambda l: l(lambda h: lambda t: lambda d: (lambda a: lambda b: b))((lambda a: lambda b: a)))(S))(lambda L: lambda R: lambda p: (lambda a: lambda b: lambda l: l(a)(b))(L)(R))(lambda L: lambda R: lambda p: _partition3(r)(S)(_partition2((lambda p: p(lambda a: lambda b: a))(S))(L)(R)(p))(p)))

_partition4 = (lambda A: lambda LR: (lambda a: lambda b: lambda l: l(a)(b))((lambda p: p(lambda a: lambda b: a))(LR))((lambda a: lambda b: lambda l: l(a)(b))((lambda p: p(lambda a: lambda b: a))(A))((lambda p: p(lambda a: lambda b: b))(LR))))

partition = lambda A:((lambda A: lambda LR: (lambda a: lambda b: lambda l: l(a)(b))((lambda p: p(lambda a: lambda b: a))(LR))((lambda a: lambda b: lambda l: l(a)(b))((lambda p: p(lambda a: lambda b: a))(A))((lambda p: p(lambda a: lambda b: b))(LR)))))(A)(((lambda r: r(r))(lambda r: lambda S: (lambda c: lambda t: lambda e: c(t)(e))((lambda l: l(lambda h: lambda t: lambda d: (lambda a: lambda b: b))((lambda a: lambda b: a)))(S))(lambda L: lambda R: lambda p: (lambda a: lambda b: lambda l: l(a)(b))(L)(R))(lambda L: lambda R: lambda p: (lambda r: lambda S: lambda LR: lambda p: r(r)((lambda p: p(lambda a: lambda b: b))(S))((lambda p: p(lambda a: lambda b: a))(LR))((lambda p: p(lambda a: lambda b: b))(LR))(p))(r)(S)((lambda x: lambda L: lambda R: lambda p: (lambda c: lambda t: lambda e: c(t)(e))((lambda m: lambda n: (lambda a: lambda b: a(b)((lambda a: lambda b: b)))((lambda m: lambda n: (lambda n: n(lambda x: (lambda a: lambda b: b))((lambda a: lambda b: a)))((lambda m: lambda n: n((lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda y: x)(lambda y: y)))(m))(m)(n)))(m)(n))((lambda a: a((lambda a: lambda b: b))((lambda a: lambda b: a)))((lambda m: lambda n: (lambda a: lambda b: a(b)((lambda a: lambda b: b)))((lambda m: lambda n: (lambda n: n(lambda x: (lambda a: lambda b: b))((lambda a: lambda b: a)))((lambda m: lambda n: n((lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda y: x)(lambda y: y)))(m))(m)(n)))(m)(n))((lambda m: lambda n: (lambda n: n(lambda x: (lambda a: lambda b: b))((lambda a: lambda b: a)))((lambda m: lambda n: n((lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda y: x)(lambda y: y)))(m))(m)(n)))(n)(m)))(m)(n))))(x)(p))((lambda a: lambda b: lambda l: l(a)(b))((lambda a: lambda b: lambda l: l(a)(b))(x)(L))(R))((lambda a: lambda b: lambda l: l(a)(b))(L)((lambda a: lambda b: lambda l: l(a)(b))(x)(R))))((lambda p: p(lambda a: lambda b: a))(S))(L)(R)(p))(p))))((lambda p: p(lambda a: lambda b: b))(A))((lambda a: lambda b: b))((lambda a: lambda b: b))((lambda p: p(lambda a: lambda b: a))(A)))

_quicksort = lambda r: lambda A: lambda LR: ((lambda r: r(r)) (lambda r: lambda l1: (lambda c: lambda t: lambda e: c(t)(e))((lambda l: l(lambda h: lambda t: lambda d: (lambda a: lambda b: b))((lambda a: lambda b: a)))(l1))(lambda l2: l2)((lambda r: lambda l2: (lambda a: lambda b: lambda l: l(a)(b))((lambda p: p(lambda a: lambda b: a))(l1))(r(r)((lambda p: p(lambda a: lambda b: b))(l1))(l2)))(r))))(r(r)((lambda p: p(lambda a: lambda b: a))(LR)))((lambda a: lambda b: lambda l: l(a)(b))((lambda p: p(lambda a: lambda b: a))((lambda p: p(lambda a: lambda b: b))(LR)))(r(r)((lambda p: p(lambda a: lambda b: b))((lambda p: p(lambda a: lambda b: b))(LR)))))

_quicksort2 = lambda r: lambda A: (lambda c: lambda t: lambda e: c(t)(e))((lambda l: l(lambda h: lambda t: lambda d: (lambda a: lambda b: b))((lambda a: lambda b: a)))(A))(lambda A: A)(lambda A: (lambda c: lambda t: lambda e: c(t)(e))((lambda l: l(lambda h: lambda t: lambda d: (lambda a: lambda b: b))((lambda a: lambda b: a)))((lambda p: p(lambda a: lambda b: b))(A)))(A)((lambda r: lambda A: lambda LR: (lambda c: lambda t: lambda e: c(t)(e))((lambda l: l(lambda h: lambda t: lambda d: (lambda a: lambda b: b))((lambda a: lambda b: a)))(r(r)((lambda p: p(lambda a: lambda b: a))(LR))))((lambda a: lambda b: lambda l: l(a)(b))((lambda p: p(lambda a: lambda b: a))((lambda p: p(lambda a: lambda b: b))(LR)))(r(r)((lambda p: p(lambda a: lambda b: b))((lambda p: p(lambda a: lambda b: b))(LR)))))(((lambda r: r(r)) (lambda r: lambda l1: (lambda c: lambda t: lambda e: c(t)(e))((lambda l: l(lambda h: lambda t: lambda d: (lambda a: lambda b: b))((lambda a: lambda b: a)))((lambda p: p(lambda a: lambda b: b))(l1)))(lambda l2: (lambda a: lambda b: lambda l: l(a)(b))((lambda p: p(lambda a: lambda b: a))(l1))(l2))((lambda r: lambda l2: (lambda a: lambda b: lambda l: l(a)(b))((lambda p: p(lambda a: lambda b: a))(l1))(r(r)((lambda p: p(lambda a: lambda b: b))(l1))(l2)))(r))))(r(r)((lambda p: p(lambda a: lambda b: a))(LR)))((lambda a: lambda b: lambda l: l(a)(b))((lambda p: p(lambda a: lambda b: a))((lambda p: p(lambda a: lambda b: b))(LR)))(r(r)((lambda p: p(lambda a: lambda b: b))((lambda p: p(lambda a: lambda b: b))(LR)))))))(r)(A)((lambda A:((lambda A: lambda LR: (lambda a: lambda b: lambda l: l(a)(b))((lambda p: p(lambda a: lambda b: a))(LR))((lambda a: lambda b: lambda l: l(a)(b))((lambda p: p(lambda a: lambda b: a))(A))((lambda p: p(lambda a: lambda b: b))(LR)))))(A)(((lambda r: r(r))(lambda r: lambda S: (lambda c: lambda t: lambda e: c(t)(e))((lambda l: l(lambda h: lambda t: lambda d: (lambda a: lambda b: b))((lambda a: lambda b: a)))(S))(lambda L: lambda R: lambda p: (lambda a: lambda b: lambda l: l(a)(b))(L)(R))(lambda L: lambda R: lambda p: (lambda r: lambda S: lambda LR: lambda p: r(r)((lambda p: p(lambda a: lambda b: b))(S))((lambda p: p(lambda a: lambda b: a))(LR))((lambda p: p(lambda a: lambda b: b))(LR))(p))(r)(S)((lambda x: lambda L: lambda R: lambda p: (lambda c: lambda t: lambda e: c(t)(e))((lambda m: lambda n: (lambda a: lambda b: a(b)((lambda a: lambda b: b)))((lambda m: lambda n: (lambda n: n(lambda x: (lambda a: lambda b: b))((lambda a: lambda b: a)))((lambda m: lambda n: n((lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda y: x)(lambda y: y)))(m))(m)(n)))(m)(n))((lambda a: a((lambda a: lambda b: b))((lambda a: lambda b: a)))((lambda m: lambda n: (lambda a: lambda b: a(b)((lambda a: lambda b: b)))((lambda m: lambda n: (lambda n: n(lambda x: (lambda a: lambda b: b))((lambda a: lambda b: a)))((lambda m: lambda n: n((lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda y: x)(lambda y: y)))(m))(m)(n)))(m)(n))((lambda m: lambda n: (lambda n: n(lambda x: (lambda a: lambda b: b))((lambda a: lambda b: a)))((lambda m: lambda n: n((lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda y: x)(lambda y: y)))(m))(m)(n)))(n)(m)))(m)(n))))(x)(p))((lambda a: lambda b: lambda l: l(a)(b))((lambda a: lambda b: lambda l: l(a)(b))(x)(L))(R))((lambda a: lambda b: lambda l: l(a)(b))(L)((lambda a: lambda b: lambda l: l(a)(b))(x)(R))))((lambda p: p(lambda a: lambda b: a))(S))(L)(R)(p))(p))))((lambda p: p(lambda a: lambda b: b))(A))((lambda a: lambda b: b))((lambda a: lambda b: b))((lambda p: p(lambda a: lambda b: a))(A))))(A))))

quicksort = (lambda r: r(r))(lambda r: lambda A: (lambda r: lambda A: (lambda c: lambda t: lambda e: c(t)(e))((lambda l: l(lambda h: lambda t: lambda d: (lambda a: lambda b: b))((lambda a: lambda b: a)))(A))(lambda A: A)(lambda A: (lambda c: lambda t: lambda e: c(t)(e))((lambda l: l(lambda h: lambda t: lambda d: (lambda a: lambda b: b))((lambda a: lambda b: a)))((lambda p: p(lambda a: lambda b: b))(A)))(A)((lambda r: lambda A: lambda LR: (lambda c: lambda t: lambda e: c(t)(e))((lambda l: l(lambda h: lambda t: lambda d: (lambda a: lambda b: b))((lambda a: lambda b: a)))(r(r)((lambda p: p(lambda a: lambda b: a))(LR))))((lambda a: lambda b: lambda l: l(a)(b))((lambda p: p(lambda a: lambda b: a))((lambda p: p(lambda a: lambda b: b))(LR)))(r(r)((lambda p: p(lambda a: lambda b: b))((lambda p: p(lambda a: lambda b: b))(LR)))))(((lambda r: r(r)) (lambda r: lambda l1: (lambda c: lambda t: lambda e: c(t)(e))((lambda l: l(lambda h: lambda t: lambda d: (lambda a: lambda b: b))((lambda a: lambda b: a)))((lambda p: p(lambda a: lambda b: b))(l1)))(lambda l2: (lambda a: lambda b: lambda l: l(a)(b))((lambda p: p(lambda a: lambda b: a))(l1))(l2))((lambda r: lambda l2: (lambda a: lambda b: lambda l: l(a)(b))((lambda p: p(lambda a: lambda b: a))(l1))(r(r)((lambda p: p(lambda a: lambda b: b))(l1))(l2)))(r))))(r(r)((lambda p: p(lambda a: lambda b: a))(LR)))((lambda a: lambda b: lambda l: l(a)(b))((lambda p: p(lambda a: lambda b: a))((lambda p: p(lambda a: lambda b: b))(LR)))(r(r)((lambda p: p(lambda a: lambda b: b))((lambda p: p(lambda a: lambda b: b))(LR)))))))(r)(A)((lambda A:((lambda A: lambda LR: (lambda a: lambda b: lambda l: l(a)(b))((lambda p: p(lambda a: lambda b: a))(LR))((lambda a: lambda b: lambda l: l(a)(b))((lambda p: p(lambda a: lambda b: a))(A))((lambda p: p(lambda a: lambda b: b))(LR)))))(A)(((lambda r: r(r))(lambda r: lambda S: (lambda c: lambda t: lambda e: c(t)(e))((lambda l: l(lambda h: lambda t: lambda d: (lambda a: lambda b: b))((lambda a: lambda b: a)))(S))(lambda L: lambda R: lambda p: (lambda a: lambda b: lambda l: l(a)(b))(L)(R))(lambda L: lambda R: lambda p: (lambda r: lambda S: lambda LR: lambda p: r(r)((lambda p: p(lambda a: lambda b: b))(S))((lambda p: p(lambda a: lambda b: a))(LR))((lambda p: p(lambda a: lambda b: b))(LR))(p))(r)(S)((lambda x: lambda L: lambda R: lambda p: (lambda c: lambda t: lambda e: c(t)(e))((lambda m: lambda n: (lambda a: lambda b: a(b)((lambda a: lambda b: b)))((lambda m: lambda n: (lambda n: n(lambda x: (lambda a: lambda b: b))((lambda a: lambda b: a)))((lambda m: lambda n: n((lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda y: x)(lambda y: y)))(m))(m)(n)))(m)(n))((lambda a: a((lambda a: lambda b: b))((lambda a: lambda b: a)))((lambda m: lambda n: (lambda a: lambda b: a(b)((lambda a: lambda b: b)))((lambda m: lambda n: (lambda n: n(lambda x: (lambda a: lambda b: b))((lambda a: lambda b: a)))((lambda m: lambda n: n((lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda y: x)(lambda y: y)))(m))(m)(n)))(m)(n))((lambda m: lambda n: (lambda n: n(lambda x: (lambda a: lambda b: b))((lambda a: lambda b: a)))((lambda m: lambda n: n((lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda y: x)(lambda y: y)))(m))(m)(n)))(n)(m)))(m)(n))))(x)(p))((lambda a: lambda b: lambda l: l(a)(b))((lambda a: lambda b: lambda l: l(a)(b))(x)(L))(R))((lambda a: lambda b: lambda l: l(a)(b))(L)((lambda a: lambda b: lambda l: l(a)(b))(x)(R))))((lambda p: p(lambda a: lambda b: a))(S))(L)(R)(p))(p))))((lambda p: p(lambda a: lambda b: b))(A))((lambda a: lambda b: b))((lambda a: lambda b: b))((lambda p: p(lambda a: lambda b: a))(A))))(A)))))(r)(A)(A))
