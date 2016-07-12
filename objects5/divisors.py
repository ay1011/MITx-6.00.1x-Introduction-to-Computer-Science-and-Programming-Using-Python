## Tuples
## divisors

def findDivisors(n1, n2):
    """assumes that n1 and n2 are positive ints
       returns a tuple containing the common divisors of n1 and n2"""
    divisors = () # the empty tuple
    for i in range(1, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            divisors = divisors + (i,)
    return divisors


divisors = findDivisors(20, 100)
print divisors
total = 0
for d in divisors:
    total += d
print(total)

## List
## universities
Techs = ['MIT', 'Cal Tech']
Ivys = ['Harvard', 'Yale', 'Brown']

Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Cal Tech'], ['Harvard', 'Yale', 'Brown']]

Techs.append('RPI')

print('Univs = ')
print(Univs)
print('')
print('Univs1 =')
print(Univs1)


for e in Univs:
    print('Univs contains ')
    print(e)
    print('   which contains')
    for u in e:
        print('      ' + u)

def removeDups(L1, L2):
    ori_L1= L1[:]            # clones L1
    for e1 in ori_L1:
        if e1 in L2:
            L1.remove(e1)
L1 = [1,2,3,4]
L2 = [1,2,5,6]
removeDups(L1, L2)
print L1



## functions as object
# applyToEach

def applyToEach(L, f):
    """assumes L is a list, f a function
       mutates L by replacing each element, e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])


L = [1, -2, 3.4]

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

applyToEach(L, abs)
print(L)

applyToEach(L, int)
print(L)

applyToEach(L, fact)
print(L)

applyToEach(L, fib)
print(L)


def applyFuns(L, x):
    for f in L:
        print(f(x))
applyFuns([abs, int, fact, fib], 4)


print map(abs, [1, -2, 3, -4])
L1	=	[1,	28,	36]
L2	=	[2,	57,	9]
print map(min,	L1,	L2)

## Dictionary
monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 1:'Jan', 2:'Feb', 3:'Mar'}
monthNumbers['Apr'] = 4
collect = []
for e in monthNumbers:
    collect.append(e)
print collect
print monthNumbers.keys()

myDict = {(1,2): 'twelve', (1,3): 'thirteen'}
print myDict[(1,2)]