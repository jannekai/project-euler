from collections import OrderedDict
import time
import math
from euler import *
start = time.time()

def triangle(n):    return int(n*(n+1)/2)
def square(n):      return int(n*n)
def pentagonal(n):  return int(n*(3*n-1)/2)
def hexagonal(n):   return int(n*(2*n-1))
def heptagonal(n):  return int(n*(5*n-3)/2)
def octagonal(n):   return int(n*(3*n-2))

i = 1
triangles = []
squares = []
pentagonals = []
heptagonals = []
octagonals = []
while True:
    i += 1
    break

i = 0    
d = OrderedDict()
while True:
    i += 1
    t = triangle(i)
    s = square(i)
    p = pentagonal(i)
    h = hexagonal(i)
    o = octagonal(i) 

end = time.time() - start
print ("Total time was " + str(end)+ " seconds")
    
