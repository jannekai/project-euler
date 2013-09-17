import time
import math
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

def isTruncatable(x):
    global p
    t = [x]
    c = 0
    n = x / 10
    while n > 0:
        if n not in p:
            return False
        t.append(n)
        n = n / 10
        c += 1

    c = 10**c
    n = x - (x/c*c)
    while c > 1:
        if n not in p:
            return False
        t.append(n)        
        c = c / 10
        n = n - (n/c*c)

    print t
    return True
    
gen = primes()
s = 0
c = 0
p = set()
while c < 11:
    x = gen.next()
    p.add(x)
    if x > 7 and isTruncatable(x):
        print "Found %d" % x
        c += 1
        s += x

print "Sum is %d, total of %d primes were calculated" % (s, len(p))

end = time.time() - start
print "Total time was " + str(end)+ " seconds"
    
