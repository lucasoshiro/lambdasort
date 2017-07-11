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
