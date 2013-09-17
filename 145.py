from collections import OrderedDict
import time
import math
from euler import *
start = time.time()

def isReversible(x):
    v = str(int(x) + int(x[::-1]))
    if '0' in v:    return False
    if '2' in v:    return False
    if '4' in v:    return False
    if '6' in v:    return False
    if '8' in v:    return False
    return True
    

c = 0
m = 10**9
m = 10**8
# m = 10**7
# m = 1000
n = 10
p = 1
for i in range(0, m):
    if i >= n:
        p  = n
        n *= 10
    if i % 1000000 == 0:
        print(i, c)
    if i % 10 == 0:
        continue
    if int(i / p) % 2 == i % 2:
        continue    
    if isReversible(str(i)):
        c  += 1
print(c)
end = time.time() - start
print ("Total time was " + str(end)+ " seconds")
