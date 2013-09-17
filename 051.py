import time
import math
from euler import *

start = time.time()

def testprime(x):
	l = len(x)
	
	# Two digit replacements changes
	for a in range(0, l):
		for b in range(a+1, l):
			f = set()
			for n in range(0, 9):
				v = list(x)
				v[a] = n
				v[b] = n
				v = listtostring(v)				
				if v in pset:
					f.add(v)
			if len(f) == 8:
				print(f)				
				return True
			print(a,b,f)			

	# Three digit replacements changes
	for a in range(0, l):
		for b in range(a+1, l):
			for c in range(b+1, l):
				f = set()
				for n in range(0, 9):
					v = list(x)
					v[a] = n
					v[b] = n
					v[c] = n
					v = listtostring(v)				
					if v in pset:
						f.add(v)
				if len(f) == 8:
					print(f)
					return True
				print(a,b,c,f)

	# Four digit replacements changes
	for a in range(0, l):
		for b in range(a+1, l):
			for c in range(b+1, l):
				for d in range(c+1, l):
					f = set()
					for n in range(0, 9):
						v = list(x)
						v[a] = n
						v[b] = n
						v[c] = n
						v[d] = n
						v = listtostring(v)				
						if v in pset:
							f.add(v)
					if len(f) == 8:
						print(f)
						return True
					print(a,b,c,d,f)

	# Five digit replacements changes
	for a in range(0, l):
		for b in range(a+1, l):
			for c in range(b+1, l):
				for d in range(c+1, l):
					for e in range(d+1, l):
						f = set()
						for n in range(0, 9):
							v = list(x)
							v[a] = n
							v[b] = n
							v[c] = n
							v[d] = n
							v[e] = n
							v = listtostring(v)				
							if v in pset:
								f.add(v)
						if len(f) == 8:
							print(f)
							return True
						print(a,b,c,d,e,f)					

	return False

primes = primeList()
plist = list()
pset = set()
for p in primes:
	pset.add(str(p))
	if p < 100000:
		continue	
	if p > 999999:
		break	
	plist.append(inttolist(p))
	
testprime([1,2,1,3,1,3])

for p in plist:
	break
	if testprime(p):
		print(p)
		break
		
end = time.time() - start
print ("Total time was " + str(end)+ " seconds")

