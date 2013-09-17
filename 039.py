import time
import math
start = time.time()

# p = a + b + c
# c = sqrt(a*a + b*b)

maxsolutions = 0
maxp = 0
for p in range(2, 1001):	
	c = 0
	for a in range(1, 1001):		
		if a > p:
			break
		for b in range(a, 1001):
			v = a + b + math.sqrt(a*a + b*b) 			
			if v > p:
				break
			if v == p:
				c += 1
	if c > maxsolutions:
		maxsolutions = c
		maxp =  p
	if p % 100 == 0:
		print maxp

print maxsolutions
print maxp
end = time.time() - start
print "Total time was " + str(end)+ " seconds"
    
    

