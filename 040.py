import time
import math
import sys

start = time.time()

s = ""
i = 1
while len(s) < 1000000:
	s += str(i)
	i += 1

print s[0]
print s[9]
print s[99]
print s[999]
print s[9999]
print s[99999]
print s[999999]
 
print int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])
 
end = time.time() - start
print "Total time was " + str(end)+ " seconds"
    
