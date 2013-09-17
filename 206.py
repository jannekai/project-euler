import time
import math
start = time.time()

numbers = [x for x in range(1, 101)]

v = int(math.sqrt(1929374254627488900))
print(v)
print(v*v)
print(1929374254627488900, math.sqrt(1929374254627488900))

def findsqr():
	for a in range(0, 10):		
		for b in range(0, 10):
			for c in range(0, 10):
				print(a,b,c)
				for d in range(0, 10):
					for e in range(0, 10):
						for f in range(0, 10):
							for g in range(0, 10):
								for h in range(0, 10):
									for i in range(0, 10):
										v = 1020304050607080900
										v += a*10
										v += b*1000
										v += c*100000
										v += d*10000000
										v += e*1000000000
										v += f*100000000000
										v += g*10000000000000
										v += h*1000000000000000
										v += i*100000000000000000
										s = int(math.sqrt(v))
										if s*s == v:
											print(v)									
											return

findsqr()
end = time.time() - start
print ("Total time was " + str(end)+ " seconds")
    
