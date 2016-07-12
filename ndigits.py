"""
function ndigits takes an integer x (either positive or negative)
and returns the number of digits in x
"""
def ndigits(x):
    # changes the sign of negative integers
    if x < 0:
        x=-x
    # base case: single digit integers
    if x < 10:
        return 1
    # recursively call ndigits(x/10) until base case obtained
    else:
        return ndigits(x/10) + 1

print ndigits(0)


