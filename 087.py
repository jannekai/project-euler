import time
import math
from euler import *
start = time.time()

plist = primeList()
r = set()
m = 50*10**6
# m = 100
for p1 in plist:
	v1 = p1**2
	if v1 >= m:
		break
	for p2 in plist:
		v2 = p2**3
		if v1 + v2 >= m:				
			break
		for p3 in plist:
			v = v1 + v2 + p3**4
			if v >= m:
				break
			r.add(v)
			if len(r) % 10000 == 0:
				print(len(r), v, p1, p2, p3)
			
		
print(len(r))
		
end = time.time() - start
print ("Total time was " + str(end)+ " seconds")
