def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    return aTup[::2]
    #return tuple([aTup[i] for i in range(len(aTup)) if i % 2 ==0])
    """
    collect = ()
    for i in range(len(aTup)):
        if i % 2 ==0:
            collect += (aTup[i],)
    return collect
    """

print oddTuples(('I', 'am', 'a', 'test', 'tuple'))

x = [1, 2, [3, 'John', 4], 'Hi']
print range(10, 3, -1)

aList = range(1, 6)
print aList
bList = aList
print bList
aList[2] = 'hello'
print aList
print aList == bList
print bList

listA = [1, 4, 3, 0]
print listA.sort
print listA
print listA.sort()
print listA
print listA.insert(0, 100)
print listA
listA.remove(3)
print listA
listA.append(7)
print listA

listB = ['x', 'z', 't', 'q']
print listB.sort()
print listB
print listB.pop()
print listB
print listB.count('a')
#print listB.remove('a')
print listB

listA.extend([4, 1, 6, 3, 4])
print listA
print listA.count(4)
print listA.index(1)
print listA.pop(4)
print listA
print listA.reverse()
print listA


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
def f(x):
    return abs(x)
def g(x):
    return x+1



testList = [1, -4, 8, -9]
applyToEach(testList, f)
print testList
testList = [1, -4, 8, -9]
applyToEach(testList, g)
print testList

animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'
print animals
#print animals['donkey']
print animals.keys()
animals['a'] = 'anteater'
del animals['b']
print animals.values()


def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    #return sum([1 for key in aDict for elem in aDict[key]])
    return sum([len(aDict[key]) for key in aDict ])
    """
    count = 0
    for key in aDict:
       count+=len(aDict[key])
    return count
    """



animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print howMany(animals)


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here

    if len(aDict) == 0:
        return None
    count = []
    for key in aDict.keys():
        count.append(len(aDict[key]))
    return aDict.keys()[count.index(max(count))]


    """
    res = None
    Val = 0
    for key in aDict.keys():
        if len(aDict[key]) >= Val:
            res = key
            Val = len(aDict[key])
    return res
    """

print biggest(animals)