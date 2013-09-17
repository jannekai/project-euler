import time
import math
from euler import *

start = time.time()

def testkey(k, l):
	c  = 0
	s = str(k)	
	d = int(s[c])
	for k in l:
		if d == k:
			c += 1
		if c < 3:
			d = int(s[c])
		else:
			return True
	return False
		
keylist = []
passcode =  [7]
tmp = set([319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716])
for i in tmp: 
	keylist.append(str(i))

# Find the first digit of passcode 
for i in range(0, len(keylist)):
	d1 = keylist[i][0]
	foundMatch = False
	
	for k in range(0, len(keylist)):
		d2 = keylist[k][1]
		d3 = keylist[k][2]
		
		if d1 == d2 or d1 == d3:
			foundMatch = True
			break
	
	if foundMatch == False:
		print d1
		break
	
# Find the last digit of passcode 
for i in range(len(keylist)-1, -1, -1):
	d1 = keylist[i][2]
	foundMatch = False
	
	for k in range(len(keylist)-1, -1, -1):
		d2 = keylist[k][0]
		d3 = keylist[k][1]
		
		if d1 == d2 or d1 == d3:
			foundMatch = True
			break
	
	if foundMatch == False:
		print d1
		break

# The passcode must be in the format of 7XXXXX0
codes = []
for a in range(0, 10):
	for b in range(0, 10):
		for c in range(0, 10):
			for d in range(0, 10):
				for e in range(0, 10):
					for f in range(0, 10):
						foundCode = True
						for i in keylist:
							if testkey(i, [7, a, b, c, d, e, f, 0]) == False:
								foundCode = False
								break		
						if foundCode == True:
							print [7, a, b, c, d, e, f, 0]
			
end = time.time() - start
print "Total time was " + str(end)+ " seconds"

# 
# 129, 389, 769, 790, 160, 289, 
# 290, 680, 689, 690, 180, 316, 
# 318, 319, 710, 716, 162, 718, 
# 719, 720, 728, 729, 731, 890, 
# 736, 362, 620, 368, 168, 629, 
# 760, 762, 380

# 73162890
