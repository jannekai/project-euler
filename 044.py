import time
import math
import sys
from euler import *

# 2166 1019 1147

start = time.time()

p = []
for i in range(1, 1000000):
	p.append(int((3*i*i-i)/2))

t = set(p)
m = 987654321
for i in range(0, len(p)-1500):
	if i % 10000 == 0:
		print(i)
	for k in range(i+1, i+1500):				
		if p[i]+p[k] in t and p[k]-p[i] in t:
			print(k,i,math.fabs(p[k]-p[i]))
			if math.fabs(p[k]-p[i]) < m:
				m = math.fabs(p[k]-p[i])
				print(k,i,math.fabs(p[k]-p[i]))

end = time.time() - start
print("Total time was " + str(end)+ " seconds")
    
