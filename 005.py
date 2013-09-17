import time

start = time.time()
v = 1
d = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

found = False
while found == False:
    v += 1
    found = True
    if v%100000 == 0: print v
    for i in d:
        if v % i != 0:
            found = False
            break

end = time.time()-start
print "Found " + str(v) + " in " + str(end) + " seconds"

