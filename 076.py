import time
import math
start = time.time()

r = dict()
r[1] = list([(1)])
r[2] = list([(2), (1,1)])
r[3] = list([(3), (1,1,1), (2,1)])
r[4] = list([(4), (1,1,1,1), (2,1,1), (2,2), (3,1)])
r[5] = list([(5), (1,1,1,1,1), (2,1,1,1), (2,2,1), (3,1,1), (3,2), (4,1)])

print(r)

end = time.time() - start
print ("Total time was " + str(end)+ " seconds")
    
