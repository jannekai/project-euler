import time
import math
from euler import *
start = time.time()

def isIncreasing(x, l):
	for i in range(0, l-1):
		if x[i] > x[i+1]:
			return False
	return True
		
def isDecreasing(x, l):
	for i in range(0, l-1):
		if x[i] < x[i+1]:
			return False
	return True
 		   	
n = 0
b = 0
while True:
	n += 1
	x = inttolist(n)
	l = len(x)
	if isIncreasing(x, l):
		#print("Inc: ", n, x)
		continue
	if isDecreasing(x, l): 	
		#print("Dec: ", n, x)
		continue
	
	b += 1

	if b / n >= 0.99:
		print(n, b, n / b)
		break


end = time.time() - start
print ("Total time was " + str(end)+ " seconds")    