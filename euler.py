import math
import random
import pickle

plist = None
pset = None

# Loads primes from pregenerated cache
def primeList():
	f = open("prime-list.txt", "rb")
	l = pickle.load(f)
	f.close()
	return l

# Loads primes from pregenerated cache
def primeSet():
	f = open("prime-set.txt", "rb")
	s = pickle.load(f)
	f.close()
	return s

# Returns true or false if the given number is a prime or not
def isPrime(n):
	if n < 2:
		return False
	if n == 2:
		return True
	if not n & 1:
		return False	
	for i in range(3, int(n**0.5)+1, 2):
		if n % i == 0:
			return False
	return True
	
	
# Returns a list of primes for the given range
def primesTo(maxprime):
	p = 3
	primes = [3]
	while p <= maxprime:
		p += 2
		h = int(math.sqrt(p)) + 1
		f = True
				
		for i in primes:
			if p % i == 0:
				f = False
				break
			if i > h:
				break
		
		if f == True:
			primes.append(p)
			
	primes.insert(0, 2)
	return primes

# Returns an array with primes marked
def primeArray(maxprime):
	plist = primesTo(maxprime)
	parray = [0]*maxprime
	for p in plist:
		parray[p] = p
	return parray
	
# Generates primes
def primegen():
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

# Returns the number of digits in an integer number
def digits(x):
	if x > 0: 	
		return int(math.log10(x)) + 1
	elif x == 0:
		return 0
	else:
		return int(math.log10(-x)) + 1
	
# Returns the digits of a number in a set
def digitset(x):
	r = set()
	
	if x == 0:
		r.add(0)
	else:			
		n = x				
		if x < 0:
			n = -x		
		while n > 0:
			r.add(n%10)
			n = n/10	 
	return r
	

# Returns the digits of a number in a list
def digitlist(x):
	r = [0]*10
	if x == 0:
		r[0] = 1
	else:
		n = x
		if x < 0:
			n = -x
		while n > 0:
			r[int(n%10)] += 1
			n = n/10
	return r
	
# Returns true if the number is a pan digit, ie. each digit 
# is defined only once in the list
def ispandigit(x):
	s = digitset(x)
	return len(s) == digits(x)

# Reverses an integer and returns it as integer
def reverseint(x):
	return int(str(x)[::-1])

# Returns true if the given number is palindrome
def ispalindrome(x):
	x = str(x)
	return x == x[::-1]

# Concatenates a list into int
def listtoint(l):
    return sum(digit * 10 ** (len(l) - 1 - i)
        for i, digit in enumerate(l))
	
# Breaks the digits of int to a list
def inttolist(x):
	x = str(x)
	return [int(y) for y in x]
	
def listtostring(l):
	return ''.join(map(str, l))

# Calculates the digital root of a number
def digitalroot(x):
	return 1 + ((x - 1) % 9)


def isPrimeMR(n, num_trials = 6):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime. 
    """
    assert n >= 2

    # special case 2
    if n == 2:
        return True
    
    # ensure n is odd
    if n % 2 == 0:
        return False
    
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(0, num_trials):
        a = random.randint(2, n-1)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite


# Euler's totient function eulers phi function
# First 1-99 totient numbers
# phi = [0,1,1,2,2,4,2,6,4,6,4,10,4,12,6,8,8,16,6,18,8,12,10,22,8,20,12,18,12,28,8,30,16,20,16,24,12,36,18,24,16,40,12,42,20,24,22,46,16,42,20,32,24,52,18,40,24,36,28,58,16,60,30,36,32,48,20,66,32,44,24,70,24,72,36,40,36,60,24,78,32,54,40,82,24,64,42,56,40,88,24,72,44,60,46,72,32,96,42,60]
def eulertotient(x):
	global plist, pset
	
	if plist == None:
		plist = primeList()
		pset = primeSet()
	
	if x == 1:     return 1
	if x in pset:  return x - 1
	
	t = float(x)
	n = float(x)
	d = 1
	for p in plist:		
		if p > t:
			break		
		if x % p == 0:			
			n *= (p-1)
			d *= p
			while t % p == 0: 
				t /= p
				
	return int(n/d)
	
	 