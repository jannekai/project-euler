import time
import math
start = time.time()

s = 0
m = 10
for i in range(2, 999999):
	n = i
	v = 0
	while n > 0:
		v += (n%10)**5
		n = n / 10
	if v == i:
		print i
		s += v
		
print s

end = time.time() - start
print "Total time was " + str(end)+ " seconds"
    
