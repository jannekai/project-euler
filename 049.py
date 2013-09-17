import time
import math
from euler import *

start = time.time()

p = primesto(10000)
p = [x for x in p if x > 990]
l = len(p)
for a in range(0, l):
	al = digitlist(p[a])
	for b in range(a+1, l):
		bl = digitlist(p[b])		
		if al != bl:
			continue
		for c in range(b+1, l):
			cl = digitlist(p[c])
			if al != cl:
				continue
			if p[c] - p[b] == p[b] - p[a]:
				print p[a], p[b], p[c]


end = time.time() - start
print "Total time was " + str(end)+ " seconds"

296962999629
