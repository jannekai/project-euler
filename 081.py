import time
import math
start = time.time()

# log(x,a) == y <==> a**y == x
m = [] 
for l in open("081.txt").readlines():
	m.append([int(x) for x in l.split(",")])

c = 79
for i in range(c, 0, -1):
	m[i-1][c] += m[i][c]
	m[c][i-1] += m[c][i]

for i in range(c-1, -1, -1):
	# Diagonal
	if m[i][i+1] < m[i+1][i]:
		m[i][i] += m[i][i+1]
	else:
		m[i][i] += m[i+1][i]
	
	# Columns
	for k in range(i-1, -1, -1):
		if m[k][i+1] < m[k+1][i]:
			m[k][i] += m[k][i+1]
		else:
			m[k][i] += m[k+1][i]
				
	# Rows
	for k in range(i-1, -1, -1):
		if m[i+1][k] < m[i][k+1]:
			m[i][k] += m[i+1][k]
		else:
			m[i][k] += m[i][k+1]
		 
print(m[0][0])


end = time.time() - start
print ("Total time was " + str(end)+ " seconds")
    
