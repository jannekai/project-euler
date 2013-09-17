import time
import math
import sys
from euler import *

start = time.time()

i = 0
c = 0
for i0 in range(0, 2):
	for i1 in range(0, 3):
		for i2 in range(0, 5):
			for i3 in range(0, 11):
				for i4 in range(0, 21):
					for i5 in range(0, 41):
						for i6 in range(0, 101):
							v = i0*200 + i1*100 + i2*50 + i3*20 + i4*10 + i5*5 + i6*2
							if v > 200:
								continue
							for i7 in range(0, 201):
								if v + i7 == 200:
									c += 1
									if i % 100 == 0:
										print (i0, i1, i2, i3, i4)

print(c)
									
end = time.time() - start
print("Total time was " + str(end)+ " seconds")
    
