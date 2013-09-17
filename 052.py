import time
import math
import collections
start = time.time()


def digits(x):
    d = [0]*10
    while x > 0:
        d[x%10] += 1
        x /= 10
    return d

i = 0
while True:
    i += 1
        
    a = digits(i)
    if digits(i*2) != a:
        continue
    if digits(i*3) != a:
        continue
    if digits(i*4) != a:
        continue
    if digits(i*5) != a:
        continue
    if digits(i*6) != a:
        continue
    print "Answer is %d" % i
    break
        
end = time.time() - start
print "Total time was " + str(end)+ " seconds"
    
