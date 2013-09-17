import time
import math
import sys
from euler import *

start = time.time()

def notPrimePair(a, b):
    global pset
    global tset 
    if (a, b) in tset:
        return True   
    if int(str(a) + str(b)) not in pset:
        tset.add((a, b))
        return True
    if int(str(b) + str(a)) not in pset:
        tset.add((a, b))
        return True
    return False


p = primesto(999999)
pset = set(p)
tset = set()
s = 9876543210
v = []
for i in range(0, len(p)):
    if p[i] > s:    break    
    for k in range(i+1, len(p)):
        if p[i]+p[k] > s:               break
        if notPrimePair(p[i], p[k]):    continue
        print(i,k)        
        for l in range(k+1, len(p)):
            if p[i] + p[k] + p[l] > s:      break
            if notPrimePair(p[i], p[l]):    continue
            if notPrimePair(p[k], p[l]):    continue            
            for m in range(l+1, len(p)):
                if p[i]+p[k]+p[l]+p[m] > s:     break
                if notPrimePair(p[i], p[m]):    continue
                if notPrimePair(p[k], p[m]):    continue
                if notPrimePair(p[l], p[m]):    continue                
                for n in range(m+1, len(p)):
                    if p[i]+p[k]+p[l]+p[m]+p[n] > s:    break
                    if notPrimePair(p[i], p[n]):        continue
                    if notPrimePair(p[k], p[n]):        continue
                    if notPrimePair(p[l], p[n]):        continue
                    if notPrimePair(p[m], p[n]):        continue
                    s = p[i] + p[k] + p[l] + p[m] + p[n]
                    v = [p[i], p[k], p[l], p[m], p[n]]
                    print(s, v)        
print(s, v)
end = time.time() - start
print("Total time was " + str(end)+ " seconds")

