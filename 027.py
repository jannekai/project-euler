import time
import math
from euler import *

start = time.time()

p = set(primesto(1000000))

maxprime = max(p)
maxprimes = 0
maxa = 0
maxb = 0

for a in range(-999, 1000):
	if a % 100 == 0:
		print (a, maxprimes, maxa, maxb)
		
	for b in range(-999, 1000):
		n = 0
		while True:
			v = n*n + a*n + b
			
			if a == 1 and b == 41:
				print (n, v, a, b)
			if v > maxprime:
				print v
			
			if v not in p:
				break
			n += 1	
			
		if n > maxprimes:
			maxprimes = n
			maxa = a
			maxb = b
			
print maxprimes
print maxa
print maxb
print maxa*maxb
					
end = time.time() - start
print "Total time was " + str(end)+ " seconds"

# -59231