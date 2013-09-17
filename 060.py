import time
import math
import sys
import itertools
from euler import *

def pe60():
    primes = primesTo(9999)
    for ai in range(0, len(primes)):
        a = str(primes[ai])
        print(a)
        for bi in range(ai+1, len(primes)):
            b = str(primes[bi])
            
            if isPrimeMR(int(a+b)) == False: continue
            if isPrimeMR(int(b+a)) == False: continue    
            
            for ci in range(bi+1, len(primes)):
                c = str(primes[ci])
                
                if isPrimeMR(int(a+c)) == False: continue
                if isPrimeMR(int(c+a)) == False: continue    
                
                if isPrimeMR(int(b+c)) == False: continue
                if isPrimeMR(int(c+b)) == False: continue
                    
                for di in range(ci+1, len(primes)):
                    d = str(primes[di])
                    
                    if isPrimeMR(int(a+d)) == False: continue
                    if isPrimeMR(int(d+a)) == False: continue    
                
                    if isPrimeMR(int(b+d)) == False: continue
                    if isPrimeMR(int(d+b)) == False: continue
    
                    if isPrimeMR(int(c+d)) == False: continue
                    if isPrimeMR(int(d+c)) == False: continue
                                    
                    for ei in range(di+1, len(primes)):
                        e = str(primes[ei])
                        
                        if isPrimeMR(int(a+e)) == False: continue
                        if isPrimeMR(int(e+a)) == False: continue    
                
                        if isPrimeMR(int(b+e)) == False: continue
                        if isPrimeMR(int(e+b)) == False: continue
    
                        if isPrimeMR(int(c+e)) == False: continue
                        if isPrimeMR(int(e+c)) == False: continue
    
                        if isPrimeMR(int(d+e)) == False: continue
                        if isPrimeMR(int(e+d)) == False: continue
                        
                        v = int(a) + int(b) + int(c) + int(d) + int(e)
                        print(v, a, b, c, d, e)
                        return
  
start = time.time()
pe60()
end = time.time() - start
print("Total time was " + str(end)+ " seconds")
