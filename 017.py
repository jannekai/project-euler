import time
import math
import sys

start = time.time()

w = dict()
w[1] = "one"
w[2] = "two"
w[3] = "three"
w[4] = "four"
w[5] = "five"
w[6] = "six"
w[7] = "seven"
w[8] = "eight"
w[9] = "nine"
w[10] = "ten"
w[11] = "eleven"
w[12] = "twelve"
w[13] = "thirteen"
w[14] = "fourteen"
w[15] = "fifteen"
w[16] = "sixteen"
w[17] = "seventeen"
w[18] = "eighteen"
w[19] = "nineteen"
w[20] = "twenty"
w[30] = "thirty"
w[40] = "forty"
w[50] = "fifty"
w[60] = "sixty"
w[70] = "seventy"
w[80] = "eighty"
w[90] = "ninety"

def tens(x):
	global w
	if x%10 == 0:
		return w[x//10*10]
	else:
		return w[x//10*10] + "-" + w[x%10]
	
def letters(s):
	c = 0
	for i in range(0, len(s)):
		if s[i] != " " and s[i] != "-":
			c += 1
	return c
	
n = dict()
c = letters("one thousand")
for i in range(1, 1000):
	s = ""
	if i < 20:
		s += w[i]
	elif i < 100:		
		s += tens(i)
	elif i < 1000:
		if i%100 == 0:
			s += w[i//100] + " hundred "
		else:			
			if i%100 < 20:
				s += w[i//100] + " hundred and " + w[i%100]
			else:
				s += w[i//100] + " hundred and " + tens(i%100)
	c += letters(s)

print c

end = time.time() - start
print "Total time was " + str(end)+ " seconds"
