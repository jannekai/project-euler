import time
import math
start = time.time()

cipher = [int(x) for x in open("059.txt").read().split(",")]
words = [x.strip() for x in open("059-words.txt", "r").readlines()]
data = [0]*len(cipher)
length = len(cipher)

def decrypt():
	global cipher, words, data, length
	
	for a in range(ord("a"), ord("z")+1):
		for b in range(ord("a"), ord("z")+1):
			for c in range(ord("a"), ord("z")+1):
				for i in range(0, length, 3):				
					data[i+0] = chr(cipher[i+0] ^ a)
					if i+1 >= length:   
						break
					data[i+1] = chr(cipher[i+1] ^ b)
					if i+2 >= length:   
						break
					data[i+2] = chr(cipher[i+2] ^ c)
				s = ''.join(data)
				c = 0
				for w in words:
					if s.find(w) != -1:
						c += 1
					if c > 15:
						return data
							
r = decrypt()
s = 0
for c in r:
	s += ord(c)
print(s, ''.join(r))

end = time.time() - start
print ("Total time was " + str(end)+ " seconds")
    
