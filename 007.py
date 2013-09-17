import time
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
            isPrime = True
            for i in primes:
                if n % i == 0:
                    isPrime = False
                    break
                
            # If the value was not divisible by any of the previously
            # found primes, break the inner loop
            if isPrime:                
                break

c = 0
i = 0
x = 2000000
p = primes()
v = 0
while True:
    i = p.next()
    if i >= x:
        break;
    v += i
    if c % 1000 == 0:
        print "%d = %d " % (i, v)    
    c += 1

print "%d = %d " % (i, v)

end = time.time() - start
print "Total time was " + str(end)+ " seconds"
    
