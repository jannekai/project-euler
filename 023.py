import time
import math
start = time.time()
# 4179871

def factorsum(x):
	if x == 0:
		return 0
		
	f = set()
	for i in range(1, int(math.sqrt(x))+1):
		if x % i == 0:
			f.add(i)
			f.add(x/i)
	f.remove(x)
	return sum(f)
    
# Find all abundant numbers below 28124
a = []
for i in range(0, 28124):
	if factorsum(i) > i:
		a.append(i)

print len(a)

# Generate a set containing all numbers below the
# first number which is always abundant
b = set()
for i in range(12, 28124):
	b.add(i)
	
# Remove all numbers which are a sum of two abundant numbers from the set
for i in range(1, len(a)-1):
	for j in range(i+1, len(a)):
		b.discard(a[i]+a[j])
			
print len(b)
print sum(b)
