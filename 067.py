import time
import math
start = time.time()


d = open('67.txt', 'r').readlines()
r = []
for i in d:
    t = i.strip().split(" ")
    for j in range(0, len(t)):
        t[j] = int(t[j])
    r.append(t)

i = len(r)-1
for i in range(len(r)-2, -1, -1):
    for k in range(0, len(r[i]), 1):
        if r[i+1][k+0] > r[i+1][k+1]:
            r[i][k] += r[i+1][k+0]
        else:
            r[i][k] += r[i+1][k+1]
    print r[i]

end = time.time() - start
print "Total time was " + str(end)+ " seconds"
    
