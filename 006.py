import time

start = time.time()

def sumSquares(x):
    v = 0
    for i in range(1, x):
        v += i*i;
        print str(i) + "=" +str(i*i)
    return v

def squareSums(x):
    v = 0
    for i in range(1, x):
        v += i
    return v*v

a = sumSquares(101)
b = squareSums(101)
v = b - a

print a
print b
print v

end = time.time()-start
print "Found " + str(v) + " in " + str(end) + " seconds"

