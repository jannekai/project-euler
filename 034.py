import time
import math
import operator
import sys

start = time.time()

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return reduce(operator.mul, xrange(2,n+1))

def calc(x):
	f = 0
	while x > 0:
		f += factorial(x % 10)
		x = x // 10
	return f

for i in range(3, 10000000):
	if i == calc(i):
		print i

end = time.time() - start
print "Total time was " + str(end)+ " seconds"

