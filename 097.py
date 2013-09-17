import time
import math
import collections
start = time.time()

# 7830457
# print 2**1 000 000

i = 100000
t = 2**i
v = 7830457 - i
s = t
while v > i:
	v -= i
	s = s*t

s *= 2**v
s *= 28433
s += 1

print s % 10000000000


# v = str(1 + 28433 * 2**7830457)
# print len(v)

end = time.time() - start
print "Total time was " + str(end)+ " seconds"
  
