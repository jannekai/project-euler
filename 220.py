import time
import math
start = time.time()

a = ['a', 'R', 'b', 'F', 'R']
b = ["L", "F", "a", "L", "b"]
o = ["F", "a"]

for i in range(0, 30):
	t = []
	for c in o:
		if c == "a":
			t.extend(a)
		elif c == "b":
		  t.extend(b)
		else:
			t.append(c)
	o = t
	print(i, len(o))

print(len(o))
end = time.time() - start
print ("Total time was " + str(end)+ " seconds")    