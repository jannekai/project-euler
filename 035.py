import time
import math
import sys

start = time.time()

def primes():
    primes = []    
    n = 2
    yield n
    n = 3
    while True:
        # Return the found prime and append it to the primes list
        primes.append(n)
        yield n        

        # Find the next natural number which is not divisible by any of
        # the previously found prime.
        while True:
            # The next number after prime is always even, so we can
            # optimize by not checking the even values.
            n += 2
            h = int(math.sqrt(n)) + 1
            isPrime = True
            for i in primes:
                if n % i == 0:
                    isPrime = False
                    break
                if i > h:
                    break
                
            # If the value was not divisible by any of the previously
            # found primes, break the inner loop
            if isPrime:                
                break

def digits(x):
    d = 1
    s = 10
    while s <= x:
        d += 1
        s *= 10
    return d

def isCyclicPrime(x):
    global p

    if x < 10:
        return True

    l = digits(x)-1
    n = x / 10 + (x%10)*10**l
    for i in range(0, l):
        if n not in p:
            return False
        n = n / 10 + (n % 10)*10**l
    return True
        
primegen = primes()
p = dict()
while True:
    t = primegen.next()
    if t >= 1000000:
        break
    p[t] = t

c = 0
for i in p:
    if isCyclicPrime(i):
        c += 1
        print "Is: %d" % i

print "Cyclical prime count = %d" % c
end = time.time() - start
print "Total time was " + str(end)+ " seconds"
