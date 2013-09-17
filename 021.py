import time
import math
import sys

start = time.time()

def sumdivisors(x):
    f = set()
    for i in range(1, int(math.sqrt(x))+1):
        if x % i == 0:
            f.add(i)
            f.add(x/i)
    f.remove(x)
    return sum(f)

t = 0
m = 30000
v = [0]*m
p = set()

for i in range(1, m):
    v[i] = sumdivisors(i)

for a in range(0, 10000):
    b = v[a]
    if a != b and v[b] == a:
        print (a, b)
        p.add(a)
        p.add(b)

print t
print p
print len(p)
print sum(p)

end = time.time() - start
print "Total time was " + str(end)+ " seconds"
    
