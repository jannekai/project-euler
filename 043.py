import time
import math
import sys
import itertools
from euler import *

start = time.time()
p = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

i = p[0]
s = 0
for i in p:
    if listtoint(i[7:10]) % 17 == 0:
        if listtoint(i[6:9]) % 13 == 0:
            if listtoint(i[5:8]) % 11 == 0:
                if listtoint(i[4:7]) % 7 == 0:
                    if listtoint(i[3:6]) % 5 == 0:
                        if listtoint(i[2:5]) % 3 == 0:
                            if listtoint(i[1:4]) % 2 == 0:
                                s += listtoint(i)

print(s)    
    
end = time.time() - start
print("Total time was " + str(end)+ " seconds")
    
