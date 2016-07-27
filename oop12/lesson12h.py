import math
import time
def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        temp = math.sqrt(last)
        for p in primes:
            if p<temp:
                if last % p == 0 :
                    break
        else:
            primes.append(last)
            yield last


start = time.time()
foo = genPrimes()
for n in range(30000):
    print foo.next()
#for n in genPrimes():   print n
end = time.time()
print(end - start)

