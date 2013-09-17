import time
import math
import sys
from euler import *

start = time.time()
# p = primesto(100)
# p = primesto(1000)
p = primesto(1000000)
l = len(p)
s = set(p)
m = (0, 0, 0)
for i in range(0, l-1):
	v = p[i]
	for k in range(i+1, l):
		v += p[k]
		if v > p[-1]:
			break
		if v in s and k - i > m[0]:
			m = (k - i, i, k, p[i], p[k], v)

print(m)				
end = time.time() - start
print("Total time was " + str(end)+ " seconds")
    
