import time
import math
import sys
from euler import *

start = time.time()
	
islychrel = 0
for i in range(0, 10000):
	c = 1
	v = i + reverseint(i)
	while c < 50:
		if ispalindrome(v):
			islychrel += 1
			break
		v = v + reverseint(v)
		c += 1
				
print islychrel

end = time.time() - start
print "Total time was " + str(end)+ " seconds"
    
