import time
import math
import fractions
from euler import *
start = time.time()

i = 12000
ma = 1 / 2
mi = 1 / 3
c = 0

for d in range(i, 0, -1):
	if d % 1000 == 0:
		print(d, c)
	n = int(d*mi)-1
	if n < 1:
		n = 1
	while n < i-1:
		v = n / d
		if v >= ma:
			break
		if v > mi:
			if fractions.gcd(n,d) == 1:
				c += 1		
		n += 1						
				
print(c)
end = time.time() - start
print ("Total time was " + str(end)+ " seconds")
