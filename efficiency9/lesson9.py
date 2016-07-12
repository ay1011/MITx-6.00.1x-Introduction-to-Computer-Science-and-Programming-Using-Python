def genSubsets_a(L):
    if len(L) == 0:  return [[]]                  #list of empty list
    subsets_no_extra = genSubsets_a(L[:-1])       # get all subsets without last element
    extra = L[-1:]                                # create a list of just last element
    subsets_with_extra = [subset + extra for subset in subsets_no_extra]
    return subsets_no_extra+subsets_with_extra    # combine those with last element and those without

def genSubsets_b(lst):
    # the power set of the empty set has one element, the empty set
    result = [[]]
    for x in lst:
        # for every additional element in our set
        # the power set consists of the subsets that don't
        # contain this element (just take the previous power set)
        # plus the subsets that do contain the element (use list
        # comprehension to add [x] onto everything in the
        # previous power set)
        result.extend([subset + [x] for subset in result])
    return result

def genSubsets_c(L):
    sub = [[]]
    for e in L:
        sub += [x + [e] for x in sub] # print sub
    return sub

L = range(1,17)
#print p(L)
#print genSubsets_a(L)
#print genSubsets_b(L)
#print genSubsets_c(L)



import time
# measure wall time
"""
t0 = time.time()
def p(l):
    if len(l) == 0: return [[]]
    return p(l[1:]) + [[l[0]] + x for x in p(l[1:])]
p(L)
print time.time() - t0
"""

t0 = time.time()
genSubsets_a(L)
print time.time() - t0

t0 = time.time()
genSubsets_b(L)
print time.time() - t0

t0 = time.time()
genSubsets_c(L)
print time.time() - t0


def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
print newsearch([],2)
print search([],2)

def swapSort(L):
    count =0
    """ L is a list on integers """
    print "Original L: ", L
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print L
                count +=1
    print "Final L: ", L
    print count
swapSort([1, 2, 3, 4, 5])


def modSwapSort(L):
    count = 0
    """ L is a list on integers """
    print "Original L: ", L
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print L
                count += 1
    print "Final L: ", L
    print count
modSwapSort( [5, 4, 3, 2, 1])
