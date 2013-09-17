import time
import math
import operator
start = time.time()

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return reduce(operator.mul, xrange(2,n+1))

def combinations(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))

for i in range(0, 4):
    for j in range(0, i):
        print combinations(i, j)

end = time.time() - start
print "Total time was " + str(end)+ " seconds"
    
