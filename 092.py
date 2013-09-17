# The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
# 1! + 4! + 5! = 1 + 24 + 120 = 145
#
# Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; 
# it turns out that there are only three such loops that exist:
# 169 -> 363601 -> 1454 -> 169
# 871 -> 45361  -> 871
# 872 -> 45362  -> 872
#
# It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
# 69  -> 363600 -> 1454 -> 169 -> 363601 -> 1454
# 78  -> 45360 -> 871 -> 45361 -> 871
# 540 -> 145 -> 145
#
# Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain 
# with a starting number below one million is sixty terms.
#
# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

import time
import math
import sys
from euler import *

start = time.time()
c = 0
cache = dict()
cache[1] = 1
cache[89] = 89

def squaredigits(x):
	global cache
	
	if x in cache:
		return cache[x]
	
	v = 0
	for c in str(x):
		v += int(c)*int(c)

	if v in cache:
		cache[x] = cache[v]
	else:
		cache[x] = squaredigits(v)
		
	return cache[x]

for i in range(1, 10000000):
	if i % 100000 == 0:
		print(i, c)
	if squaredigits(i) == 89:
		c += 1
		
print(c)
end = time.time() - start
print("Total time was " + str(end)+ " seconds")
    
