import time
import math
from euler import *

start = time.time()

m = 1000001
mr = 0
mi = 0
mn = 0
for i in range(1, m):
	if i % 100000 == 0:
		print(i, mi, mn, mr)
		
	e = eulertotient(i)
	v = float(i) / float(e)
	if v > mr:
		mi = i
		mr = v
		mn = e
		
print(mi, mn, mr)
	
end = time.time() - start
print ("Total time was " + str(end)+ " seconds")
