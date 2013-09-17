import time
import math
start = time.time()

def factors(x):
    f = set()
    for i in range(1, int(math.sqrt(x))+1):
        if x % i == 0:
            f.add(i)
            f.add(x/i)
    return len(f)
    
i = 0
t = 0
d = 0
while True:
    i += 1
    t += i
    d = factors(t)
    if d > 500:
        break
    if i % 100 == 0:
        print (t, d)

print "Result %d found in %d iterations for value %d" % (d, i, t)

end = time.time() - start
print "Total time was " + str(end)+ " seconds"
    
