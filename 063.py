import time
import math
import sys
from euler import *

start = time.time()

c = 0
digit = 1
while True:
    n = 0
    while True:
    	v = n**digit
    	d = digits(v)
    	if d > digit:
    		break
    	if d == digit:
    		print("Digit: ", digit, " number: ", n, " value: ", v, " value digits: ", d, " count: ", c)
    		c += 1
    	n += 1
    digit += 1
    	

		
end = time.time() - start
print("Total time was " + str(end)+ " seconds")
    
