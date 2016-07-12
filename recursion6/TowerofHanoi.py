def printMove(first, second):
    print('move from ' + str(first) + ' to ' + str(second))

def Towers(n, _from, _to, temp):
    if n == 1:
        printMove(_from, _to)
    else:
        Towers(n - 1, _from, temp, _to)
        Towers(1, _from, _to, temp)
        Towers(n - 1, temp, _to, _from)

Towers(5, "a", "b", "c")


def hanoi(n):
    if n==0:    return 0
    return 2*hanoi(n-1)+1

def fact(n):
    if n==0:    return 1
    return n*fact(n-1)

def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

print hanoi(5)
print fact(4)
print fib(12)


def isPalindrome(s):

    def toChars(s):
        s = s.lower()         # lowercase
        ans = ''              # only choose alphabets
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

print isPalindrome("Able was I ere I saw Elba")
print isPalindrome("12345654321")