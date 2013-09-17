import time
import math
import sys

sys.setrecursionlimit(10000)
start = time.time()

s = 1
i = 3
while i <= 1001:
    t = i*i
    ## print (t, (t-i+1), (t-i*2+2), (t-i*3+3))
    s += t + (t-i+1) + (t-i*2+2) + (t-i*3+3)
    i += 2

print s
end = time.time() - start
print "Total time was " + str(end)+ " seconds"

##43 44 45 46 47 48 49    
##42 21 22 23 24 25 26
##41 20  7  8  9 10 27
##40 19  6  1  2 11 28
##39 18  5  4  3 12 29
##38 17 16 15 14 13 30
##37 36 35 34 33 32 31
