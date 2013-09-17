import time
import math
start = time.time()

def onebyx(x):	
	n = 1
	c = 0
	remainders = dict()
	while True:
		d = n // x
		n = (n - x*d) * 10		
		if n == 0:
			break		
		if n in remainders:
			break
		else:
			remainders[n] = c
			c += 1
			
	# Find the first occurence of the 
	if n == 0:
		return len(remainders)
	return c - remainders[n]	

mi = 0
mv = 0
for i in range(1, 1000):
	v = onebyx(i)
	if v >= mv:
		mv = v
		mi = i

print (mi, mv)

end = time.time() - start
print "Total time was " + str(end)+ " seconds"
    
    

