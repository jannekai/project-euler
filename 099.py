import time
import math
start = time.time()

def ipow(base, exp):
	r = 1
	while exp > 0:
		print(exp)
		if exp & 1:
			r *= base
		base *= base
		exp >>= 1
	
	return r


# log(x,a) == y <==> a**y == x
i = 1
m = 0 
for l in open("099.txt").readlines():
	t = l.split(",")
	x = int(t[0])
	r = int(t[1])
	if r*math.log(x) > m:
		m = r*math.log(x)
		print(i, x, r, r*math.log(x))
	i += 1 
			 
end = time.time() - start
print ("Total time was " + str(end)+ " seconds")
    
