import time
import math
start = time.time()

def triangle(x):
	return (x*x+x)/2
	
def pentagonal(x):
	return (3*x*x-x)/2
	
def hexagonal(x):
	return 2*x*x-x
		
ti = 285
tv = 0
pi = 165
pv = 0
hi = 143
hv = 0

while True:
	ti += 1
	tv = triangle(ti)	
	
	pv = pentagonal(pi)
	while pv < tv: 
		pi += 1
		pv = pentagonal(pi)
	
	hv = hexagonal(hi)
	while hv < tv: 
		hi += 1
		hv = hexagonal(hi)

	if tv == pv and hv == tv:
		print (ti, tv, pi, pv, hi, hv)
		break
	
	if ti % 1000 == 0:
		print (ti, pi, hi)
		
end = time.time() - start
print "Total time was " + str(end)+ " seconds"