import time
import math
from euler import *

#37 36 35 34 33 32 31
#38 17 16 15 14 13 30
#39 18  5  4  3 12 29
#40 19  6  1  2 11 28
#41 20  7  8  9 10 27
#42 21 22 23 24 25 26
#43 44 45 46 47 48 49

start = time.time()

pset = primesto(100)

for i in range(3, 100):
	if i in pset:
		if isPrimeMR(i) == False:
			print(i, isPrimeMR(i))
	else:
		if isPrimeMR(i) == True:
			print(i)

diag = 1
primes = 0
for i in range(3, 1000000, +2):	
	br = i*i
	bl = br - i + 1
	tl = bl - i + 1
	tr = tl - i + 1	
	diag += 4	
	
	if isPrimeMR(bl, 10):  primes += 1
	if isPrimeMR(tl, 10):  primes += 1
	if isPrimeMR(tr, 10):  primes += 1					
	if primes / diag < 0.1: 		
		print("Done ", i, primes, diag, primes / diag)
		break 
	
	if i % 99 == 0:
		print("... ", i, primes, diag, primes / diag)

end = time.time() - start
print ("Total time was " + str(end)+ " seconds")
    
