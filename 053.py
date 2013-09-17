import time
import math
import operator
import sys

start = time.time()

# Returns the n factorial (n!) for the given argument.
# This is the same as the number of permutations for a list
# with n members.
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return reduce(operator.mul, xrange(2,n+1))

# Returns the number of _ordered_ k item subsets in the
# a list with n members.
#
# For example:
# n = 4, k = 2 = 4!/2! = 12 two element subsets in the list (1, 2, 3, 4):
# (1,2), (1,3), (1,4),
# (2,1), (2,3), (2,4),
# (3,1), (3,2), (3,4),
# (4,1), (4,2), (4, 3)
def permutations(n,k):
    return factorial(n) / factorial(n-k)

# Returns the humber of _unordered_ k item subsets in the
# list with n members
#
# For example:
# n = 4, k=2 = n!/(k!(n-k)!) = 6 two element subsets for the list (1, 2, 3, 4)
# {1,2}, {1,3}, {1,4},
# {2,3}, {2,4}, {3,4}
def combinations(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))


c = 0
for i in range(1, 101):
    for j in range(1, i):        
        if combinations(i, j) > 1000000:
            c += 1
    print (i, c)

end = time.time() - start
print "Total time was " + str(end)+ " seconds"

