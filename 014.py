import time
import math
start = time.time()

##def seq(n):
##    c = 1
##    while n != 1:
##        c += 1
##        if n % 2 == 0:
##            n = n / 2
##        else:
##            n = 3*n + 1                    
##    return c

def seq(n):
    global s
    
    if n == 1:
        return 1
    
    if n < 500000 and s[n] != -1:
        return s[n]

    if n % 2 == 0:
        c = 1 + seq(n / 2)
    else:
        c = 1 + seq(3*n + 1)
        
    if n < 500000:
        s[n] = c

    return c

s = [-1 for x in range(0, 500000)]

i = 500001
mi = 0
mv = 0
while i <= 1000000:
    i += 1
    if seq(i) >= mv:
        mi = i
        mv = seq(i)
    if i % 100000 == 0:
        print (i, mi, mv)

print "Result is " +str(mi) + " with chain of " + str(mv)

end = time.time() - start
print "Total time was " + str(end)+ " seconds"
    
