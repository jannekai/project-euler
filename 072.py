import time
import math
import fractions
from euler import *
start = time.time()

plist = primeList()
pset = primeSet()

r = -1
m = 1000001
# m = 9
for i in range(1, m):
	if i % 100000 == 0:
		print(i, r)
	e = eulertotient(i)
	r += e

print(r)

end = time.time() - start
print ("Total time was " + str(end)+ " seconds")    
