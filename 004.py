import time

def isPalindrome(a, b):
    if a*b > 100000:
        x = str(a*b)
        # print str(a) + "*" + str(b) + "=" + x
        if (x[0] != x[5]): return False
        if (x[1] != x[4]): return False
        if (x[2] != x[3]): return False
        return True    
    return False
        
start = time.time()
m = 999
v = 0
i = 0
while i <= m:
    k = 0
    while k <= i:        
        if (isPalindrome(m-i, m-k)):
            if ((m-i) * (m-k)) > v:
                v = (m-i) * (m-k)
                break
        k += 1
    i += 1
    
end = time.time()-start    
print "Found answer " +str(v) + " in " + str(end)+ " seconds"
