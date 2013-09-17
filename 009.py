import time
import math
start = time.time()

## a**2 + b**2 = c**2
## a + b + c = 1000
## c = 1000 - a - b
## a <= 1000 b <= 1000
## a**2 + b**2 = (1000 - a - b)**2
## x = -a, y = -b
## a**2 + b**2 = (1000 + x + y)**2
## a**2 + b**2 = 1000**2 + x**2 + y**2 + 2*1000*x + 2*1000*y + 2*xy
## a**2 + b**2 =1 000 000 + a**2 + b**2 - 2000*a - 2000*b + 2*-a*-b
## 1 000 000 = 2000a + 2000b + 2*-a*-b

a = 0
b = 0
f = False
for a in range(1, 1001):
    for b in range(1, 1001):
        if 1000*a + 1000*b - a*b == 500000:
            f = True
            break
    if f:
        break
            

c = 1000 - a - b

print "a = %d b = %d c = %d" % (a,b,c)
print "a + b + c = %d" % (a+b+c)
print "abc = %d" % (a*b*c)

end = time.time() - start
print "Total time was " + str(end)+ " seconds"
    
