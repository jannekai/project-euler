import time

def primes():
    n = 2
    primes = []
    while True:
        # Return the found prime and append it to the primes list
        primes.append(n)
        yield n        

        # Find the next natural number which is not divisible by any of
        # the previously found prime
        
        while True:
            n += 1
            isPrime = True
            for i in primes:
                if n % i == 0:
                    isPrime = False
                    break
                
            # If the value was not divisible by any of the previously
            # found primes, break the inner loop
            if isPrime:                
                break

##start = time.time()
##v = 600851475143                
##p = primes()
##i = p.next()
##while i <= v:
##    if v % i == 0:
##        # print "%d is divisible by %d " % (v,i)
##        v = v / i
##    i = p.next()
##
##end = time.time()-start
##print "Found answer " +str(v) + " in " + str(end)+ " seconds"
