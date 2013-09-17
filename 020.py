import time
import math
start = time.time()


v = 100
for i in range(99, 0, -1):
    v *= i

s = str(v)
v = 0
for i in range(0, len(s)):
    v += int(s[i])

print v

end = time.time() - start
print "Total time was " + str(end)+ " seconds"
    
