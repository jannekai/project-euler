import time
import math
import sys

start = time.time()

def swap(i,j):
    global l
    t = l[i]
    l[i] = l[j]
    l[j] = t

def reverse(i):
    global l
    h = (10-i)/2
    for x in range(0, h):
        swap(i+x, 9-x)
    
l = [x for x in range(0, 10)]
c = 0
m = 1000010
i = 0
j = 0

while c < m:
    if c % 100000 == 0:
        print "%4d %s" % (c, l)    

    for t in range(9, 0, -1):
        if l[t-1] < l[t]:
            i = t-1
            break
   
    for t in range(9, 0, -1):
        if l[t] > l[i]:
            j = t
            break

    swap(i,j)
    reverse(i+1)
    
    c += 1

print l
end = time.time() - start
print "Total time was " + str(end)+ " seconds"
    
