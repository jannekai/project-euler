import time
import math
import sys
import itertools
from euler import *

start = time.time()

p = 1
for n in range(10, 100):
	for d in range(10, 100):
		n1 = int(n / 10)
		n2 = int(n % 10)
		d1 = int(d / 10)
		d2 = int(d % 10)
				
		if n/d < 1 and n2 == d1 and d2 != 0 and n/d == n1/d2:
			print(n,d)

# 16 64
# 19 95
# 26 65
# 49 98
print(16*19*26*49)
print(64*95*65*98)
print(387296/38729600)
print(1/100)

end = time.time() - start

print("Total time was " + str(end)+ " seconds")
    
