import time
import math
from euler import *

start = time.time()

def sumdigits(x):
	s = 0
	while x > 0:
		s += x%10
		x = x/10
	return s

m = 0
for a in range(1, 100):
	for b in range(1, 100):
		v = sumdigits(a**b)
		if v > m:
			m = v
	
print m
end = time.time() - start
print "Total time was " + str(end)+ " seconds"
