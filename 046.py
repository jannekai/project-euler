import time
import math
import sys
from euler import *

start = time.time()

r = 9
found = False
while found == False:
	r += 2
	if r % 10000 == 0:
		print("... ", r)
	
	if isPrimeMR(r):
		continue
	
	f = 1
	while True:
		v = 2 * f**2		
		if v >= r:	
			print("Found ", r, f, v, r-v)		
			found = True
			break	
		if isPrimeMR(r-v):
			break						
		f += 1
				
end = time.time() - start
print("Total time was " + str(end)+ " seconds")
    
