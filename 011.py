import time
import math
start = time.time()


d = open('11.txt', 'r').readlines()
r = []
for i in d:
    t = i.strip().split(" ")
    for j in range(0, len(t)):
        t[j] = int(t[j])
    r.append(t)

maxval = 0

## horizontal and vertical
for x in range(0, 20):
    for y in range(0, 20):        
        # Horizontal
        if x < 17:
            p = r[y][x+0] * r[y][x+1] * r[y][x+2] * r[y][x+3]
            if p > maxval: maxval = p

        # Vertical
        if y < 17:
            p = r[y+0][x] * r[y+1][x] * r[y+2][x] * r[y+3][x]
            if p > maxval: maxval = p

        # diagonal right
        if x < 17 and y < 17:
            p = r[y+0][x+0] * r[y+1][x+1] * r[y+2][x+2] * r[y+3][x+3]
            if p > maxval: maxval = p

        # diagonal left
        if x > 2 and y < 17:
            p = r[y+0][x-0] * r[y+1][x-1] * r[y+2][x-2] * r[y+3][x-3]
            if p > maxval: maxval = p
        
print maxval

end = time.time() - start
print "Total time was " + str(end)+ " seconds"
    
