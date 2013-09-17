import time
import math
from decimal import Decimal
from euler import *
start = time.time()

def fibonacci(a, b):
    return a + b

def fibonacci9(a, b):
    return int(str(a + b)[-9:])

def isPandigitLast9(x):
    s = set(str(x)[-9:])
    s.discard('0')
    if len(s) == 9:
        return True    
    return False

def isPandigitFirst9(n):
    print(n)
    s = Decimal(5).sqrt()
    p = Decimal((1 + s) / 2)
    v = Decimal(((p**n) - ((1-p)**n)) / s)
    sign, digits, exp = v.as_tuple()
      
    r = set(digits[:9])
    r.discard(0)
    if len(r) == 9:
        print(n, r)
        return True    
    return False

a = 1
b = 1
c = 2
while True:
    c += 1       
    n = fibonacci9(a, b)
    if n > 123456789: 
        if isPandigitLast9(n):
            if isPandigitFirst9(c):
                print(c, n)
                break    
    a, b = b, n
    
end = time.time() - start
print ("Total time was " + str(end)+ " seconds")
