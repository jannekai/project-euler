import time
import math
import sys

start = time.time()

s = set()
for a in range(2, 101):
    print 
    for b in range(2, 101):
        s.add(a**b)

print len(s)

end = time.time() - start
print "Total time was " + str(end)+ " seconds"
