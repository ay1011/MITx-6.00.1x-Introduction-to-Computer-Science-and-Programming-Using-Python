from math import tan, atan
def polysum(n,s):
    return round(0.25 * n * s * s / tan(4 * atan(1) / n) + (n * s) * (n * s),4);


