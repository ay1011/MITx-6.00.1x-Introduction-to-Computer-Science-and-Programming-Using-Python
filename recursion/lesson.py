def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    res = 1
    for i in range(exp):
        res *= base
    return res
print iterPower(2, 5)


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp <= 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)
print recurPower(-2.0, 5)

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    if exp <= 0:
        return 1
    elif exp % 2 == 0:
        return recurPowerNew(base * base, exp / 2)
    return base * recurPowerNew(base, exp - 1)

print recurPowerNew(-0.32, 8)


def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    for i in range(min(a,b),0,-1):
        if a%i ==0 and b%i==0:
            return i

print gcdIter(2, 12)
print gcdIter(6, 12)
print gcdIter(9, 12)
print gcdIter(17, 12)


def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b==0:
        return a
    else:
        return gcdRecur(b, a%b)

print gcdRecur(2, 12)
print gcdRecur(6, 12)
print gcdRecur(9, 12)
print gcdRecur(17, 12)


def lenIter(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # Your code here
    val = 0
    for i in aStr:
        val += 1
    return val
print lenIter("caravan")


def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # Your code here
    if aStr == '':
        return 0
    return 1+lenRecur(aStr[1:])
print lenRecur("caravan")


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise

    What happens when the string is empty?
What happens when the string is of length 1?
What happens when the test character equals the middle character?
    '''

    # Your code here
    # Base case: If aStr is empty, we did not find the char.
    if len(aStr) == 0:
        return False
    # Base case: if aStr is of length 1, just see if the chars are equal
    elif len(aStr) == 1:
        return char == aStr
    # Base case: See if the character in the middle of aStr equals char
    elif char == aStr[len(aStr)/2]:
        return True
    # Recursive case: If the test character is smaller than the middle
    #  character, recursively search on the first half of aStr
    else:
        #print aStr[len(aStr)/2]
        if char < aStr[len(aStr)/2]:
            #print aStr[:len(aStr)/2]
            return isIn(char, aStr[:len(aStr)/2])
        else:
            #print aStr[len(aStr) / 2+1:]
            return isIn(char, aStr[len(aStr)/2+1:])

print isIn('c','abcdefghijklm')

def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string

    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # Your code here
     # If strings aren't the same length, they cannot be semordnilap
    if len(str1) != len(str2):
        return False

    # Base case: if the strings are each of length 1, check if they're equal
    if len(str1) == 1:
        return str1 == str2

    # Recursive case: check if the first letter of str1 equals the last letter
    # of str2
    if str1[0] == str2[-1]:
        return semordnilap(str1[0:-1], str2[1:])
    else:
        return False


print "isPalindrome: %s"%semordnilapWrapper('level', 'level')

def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)

def testFib(n):
    global numCalls
    for i in range(n+1):
        numCalls = 0
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print ('fib called ' + str(numCalls) + ' times')

# testFib(10)