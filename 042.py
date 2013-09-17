import time
import math
start = time.time()

def wordvalue(s):
	c = 0
	for i in range(0, len(s)): 
		c += ord(s[i]) - 64
	return c

# Read and calculate word value for each word
# Store the maximum word value so we don't need to generate more triange values
words = open('42.txt', 'r').read().split(",")
m = 0
l = []
for w in words:	
	v = wordvalue(w)
	l.append(v)
	if v > m:
		m = v

# Generate the triangle values until we have enough for lookup
i = 0
t = set()
while True:
	i += 1
	v = (i*i+i)/2
	t.add(v)
	if v > m:
		break

print sorted(t)
c = 0
for v in l:
	if v in t:
		c += 1
	
print "Found %d" % c

end = time.time() - start
print "Total time was " + str(end)+ " seconds"
    
