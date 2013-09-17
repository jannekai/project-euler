import time
import math
from euler import *

start = time.time()
	
# Check out the 	
p = permutations([1, 2, 3, 4, 5, 6, 7])
p.sort()
for i in range(len(p)-1, 0, -1):
	v = int("".join(map(str, p[i])))
	if isPrime(v):
		print "Found %d " % v
		break
	
end = time.time() - start
print "Total time was " + str(end)+ " seconds"
