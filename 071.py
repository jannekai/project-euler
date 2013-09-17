import time
import math
import fractions
from euler import *
start = time.time()

i = 1000000
ma = 3 / 7
mi = 0
r = 0
n = 1

for d in range(i, 0, -1):
	if d % 100000 == 0:
		print(d, r)
	n = int(d*mi)
	if n < 1:
		n = 1
	while n < i-1:
		v = n / d
		if v >= ma:
			break
		if v > mi:
			if gcd(n,d) == 1:
				mi = v
				r = (n/d, n, d)			
		n += 1						
				
print(r)		
end = time.time() - start
print ("Total time was " + str(end)+ " seconds")    