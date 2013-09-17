import time
import math
import sys

start = time.time()

def tobinstring(x):
    n = x
    b = int(math.log(x, 2)) + 1
    r = [0]*b
    i = 1
    while n > 0:
        r[b-i] = str(n & 1)
        n >>= 1
        i += 1
    return "".join(r)

def ispalindrome(x):
    i = 0
    l = len(x)
    h = int(len(x)/2) + 1
    for i in range(0, int(len(x)/2)+1):
        if x[i] != x[l-i-1]:
            return False
    return True


s = 0
for i in range(1, 1000000):
    if i % 100000 == 0:
        print (i, s)
    if ispalindrome(str(i)) == False:
        continue
    if ispalindrome(tobinstring(i)):
        s += i

print s

end = time.time() - start
print "Total time was " + str(end)+ " seconds"
