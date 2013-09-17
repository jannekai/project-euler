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

chains = 0
found = set()
cache = dict()
facts = dict()
facts[0] = 1
facts[1] = 1
facts[2] = facts[1]*2
facts[3] = facts[2]*3
facts[4] = facts[3]*4
facts[5] = facts[4]*5
facts[6] = facts[5]*6
facts[7] = facts[6]*7
facts[8] = facts[7]*8
facts[9] = facts[8]*9

def sumoffactorials(x):
	if x in found:
		return 0
	else:	
		found.add(x)
			
	if x not in cache:
		v = 0
		for c in str(x):
			v += facts[int(c)]
			cache[x] = v
	
	return 1 + sumoffactorials(cache[x])

for i in range(1, 1000000):
	if i % 10000 == 0:
		print("... ", i, chains)
	found = set()
	c = sumoffactorials(i)
	if c == 60:
		chains += 1			

print(chains)	
	
end = time.time() - start
print("Total time was " + str(end)+ " seconds")
    
