x = "pi"
y = "pie"
x, y = y, x
print x
print y

def f(x):
    while x > 3:
        f(x+1)
f(1)

t = ([],[1], 5)
print t[0], t[1]

def g():
    return "a"
a = g()
print type(a)

def h(x):
    a = []
    while x > 0:
        a.append(x)
        h(x-1)

s=[1,2,3]
print type(s)
s[0] = 5
print s[0]

L = [1,2,3]
d = {'a': 'b'}
def f(x):
    return 3

stuff  = ["iQ"]
for thing in stuff:
    if thing == 'iQ':
        print "Found it"

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

print Square(-7)

def isPalindrome(aString):
    '''
    aString: a string
    '''
    # Your code here
    if aString== '':
        return True
    else:
        if aString[0] == aString[-1]:
            return isPalindrome(aString[1:-1])
        else:
            return False


print isPalindrome("affsna")

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    return sum([listA[i]*listB[i] for i in range(len(listA))])
    """
    tot = 0
    for i in range(len(listA)):
        tot += listA[i]*listB[i]
    return tot
    """


listA = [1, 2, 3]
listB = [4, 5, 6]
print dotProduct(listA, listB)

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    newList = []
    for item in aList:
        if type(item) == list:
            newList.extend(flatten(item))
        else:
            newList.append(item)
    return newList

print flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])

"""
def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    intersectList = {}
    no_intersectList = {}
    for i in range(len(d1.keys())):
        for j in range(len(d2.keys())):
            if (d1.keys()[i] in d2.keys()) :#and (d2.keys()[j] in d1.keys()):
                intersectList[d1.keys()[i]] = d1.values()[i] +d2.values()[i]
            else:
                if d1.keys()[i] not in d2.keys():
                    no_intersectList[d1.keys()[i]] = d1.values()[i]
                if d2.keys()[j] not in d1.keys():
                    no_intersectList[d2.keys()[j]] = d2.values()[j]
    return (intersectList, no_intersectList)
"""
def f(a,b):
    return a + b
def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    intersectList = {}
    no_intersectList = {}
    for key in d1.keys():
        if key in d2.keys():
            intersectList[key] = f(d1[key], d2[key])
        else:
            no_intersectList[key] = d1[key]
    for key in d2.keys():
        if key not in intersectList:
            no_intersectList[key] = d2[key]
    return (intersectList, no_intersectList)

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

print dict_interdiff(d1,d2)


def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
    """
    Lnew = []
    for i in range(len(L)):
        if f(L[i]):
            Lnew.append(L[i])
    """
    #Lnew = [L[i]  for i in range(len(L)) if func(L[i])]
    Lnew = [s for s in L if f(s)]
    L[:] = Lnew
    return len(L)

#run_satisfiesF(L, satisfiesF)


def f(s):
    return 'a' in s

L = ['a', 'b', 'a']
print satisfiesF(L)
print L