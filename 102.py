import time
import math
start = time.time()

def dot(a, b):
	return a[0]*b[0] + a[1]*b[1]

def insideTriangle(a,b,c,p):
	v0 = (c[0]-a[0], c[1]-a[1])
	v1 = (b[0]-a[0], b[1]-a[1])
	v2 = (p[0]-a[0], p[1]-a[1])

	dot00 = dot(v0, v0)
	dot01 = dot(v0, v1)
	dot02 = dot(v0, v2)
	dot11 = dot(v1, v1)
	dot12 = dot(v1, v2)
	
	invDenom = 1 / (dot00 * dot11 - dot01 * dot01)
	u = (dot11 * dot02 - dot01 * dot12) * invDenom
	v = (dot00 * dot12 - dot01 * dot02) * invDenom
	
	if u > 0 and v > 0 and u + v < 1:
		return True
	return False

r = 0
p = (0, 0)
for l in open("102.txt").readlines():
	t = l.split(",")
	a = (int(t[0]), int(t[1]))
	b = (int(t[2]), int(t[3]))
	c = (int(t[4]), int(t[5]))
	
	if insideTriangle(a,b,c,p):
		r += 1

print(r)	
			 
end = time.time() - start
print ("Total time was " + str(end)+ " seconds")
    
