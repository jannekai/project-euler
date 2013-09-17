import pickle
import math

# Returns a list of primes for the given range
def primesTo(maxprime):
	global primelist
	c = 0
	p = 3
	primelist = [3]
	while p <= maxprime:		
		h = int(math.sqrt(p)) + 1
		f = True
				
		for i in primelist:
			if p % i == 0:
				f = False
				break
			if i > h:
				break
		
		if f == True:
			primelist.append(p)
		
		p += 2		
		c += 1
		if c % 100000 == 0:
			print(p)
			
	primelist.insert(0, 2)

maxPrime = 10000000
primelist = []
primesTo(maxPrime)
primeset = set(primelist)

f = open("prime-list.bin", "wb")
pickle.dump(primelist, f)
f.close()

f = open("prime-set.bin", "wb")
pickle.dump(primeset, f)
f.close()
		 
##f = open("prime-set.txt", "rb")
##t = pickle.load(f)
##f.close()
##print(t)
##
##f = open("prime-list.txt", "rb")
##t = pickle.load(f)
##f.close()
##print(t)
