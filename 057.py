import time
import math
import sys
from euler import *

start = time.time()

# 1 + 1/2 = 3/2
# 1 + 1/(2 + 1/2) = 7/5
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12
  
c = 0
n = 1
d = 2
for i in range(0, 1000):
    n += 2*d  
    n, d = d, n
    if digits(n+d) > digits(d):
        c += 1
        print((n+d, d, (n+d)/d))    

print(c)    

end = time.time() - start
print("Total time was " + str(end)+ " seconds")

