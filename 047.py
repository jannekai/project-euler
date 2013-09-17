import time
import math
from euler import *

start = time.time()

m = 1000000
plist = primesto(m)
pset  = set(plist)
r = set()
for i in range(3, m):
	if i % 10000 == 0:
		print(i)
		
	if i in pset:
		r = set()
		continue
	
	v = i	
	p = 0
	d = set()
	while v > 1:
		if v % plist[p] == 0:
			v /= plist[p]
			d.add(p)
		else:
			p += 1
					
	if len(d) == 4:
		r.add(i)
	else:
		r = set()	
	if len(r) == 4:
		break
					  
print(r)

end = time.time() - start
print ("Total time was " + str(end)+ " seconds")
    
