import time
import math
import sys
import itertools
from euler import *

start = time.time()

r = set()
p = list(itertools.permutations([1,2,3,4,5,6,7,8,9]))
for l in p:
	for i in range(0, 6):
		for k in range(i+1, 7):
			a = listtoint(l[:i+1])
			b = listtoint(l[i+1:k+1])
			c = listtoint(l[k+1:])
			if a*b == c:
				r.add(c)
				print(a, b, c)
			if a*b > c:
				break
								
print(len(r))
print(sum(r))

end = time.time() - start
print("Total time was " + str(end)+ " seconds")
    
