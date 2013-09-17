s = 0
def fibonacci(a, b):
    global s
    if (b > 4000000):
        return
    if (b % 2 == 0):
        s += b
        print("%d sum = %d" % (b,s))        
    else:
        print(b)
    fibonacci(b, a+b)

fibonacci(1, 2)
print("total sum is %d" % s)
