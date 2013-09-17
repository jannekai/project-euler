import time
import math
import sys

sys.setrecursionlimit(10000)
start = time.time()

def fibonacci(a, b):
    global m, i
    i += 1
    if i % 1000 == 0:
        print (i, a, b)
    if (a + b) >= m:
        print (i, a, b)
        print len(str(a+b))
        return
    return fibonacci(b, a + b)

m = 10**999
#m = 144
i = 2
fibonacci(1, 1)
    
end = time.time() - start
print "Total time was " + str(end)+ " seconds"
    
