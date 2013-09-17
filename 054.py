import time
import math
start = time.time()

def cardvalue(c):
	if   c[0] == "A":  return 14
	elif c[0] == "K":  return 13
	elif c[0] == "Q":  return 12
	elif c[0] == "J":  return 11
	elif c[0] == "T":  return 10
	return int(c[0])
		
def isStraight(cards):
	if cards[0] == 14 and cards[-1] != 2:
		return False
	if cards[0] != cards[1]+1:
		return False
	for i in range(1, len(cards)-1):
		if cards[i] != cards[i+1]+1:
	   	   return False	
	return True
			
# Returns a list with boolean or card value set in descending rank
# 0 = Royal flush
# 1 = Straight flush
# 2 = Four of a kind
# 3 = Full house
# 4 = Flush
# 5 = Straight
# 6 = Three of a kind
# 7 = Two pairs (bigger of them)
# 8 = One pair
def handscore(h):	
	hv = [0]*9
	count = dict()
	cards = list()
	suits = set()
	
	for c in h:		
		v = cardvalue(c[0])
		cards.append(v)
		suits.add(c[1])
		if v not in count:
			count[v] = 1
		else:
			count[v] += 1
				
	cards.sort()
	cards.reverse()
			
	if isStraight(cards):	
		print(hv, h)
		if len(suits) == 1:
			# Royal flush			
			if cards[0] == 14:
				hv[0] = cards[0]
			# Straight flush
			else:
				hv[1] = cards[0]
		# Straight
		else:			
			hv[5] = cards[0]			
	# Flush			
	elif len(suits) == 1:		
		hv[4] = 1		
	else:		
		for v, c in count.items():
			# Four of a kind
			if c == 4:
				hv[2] = v
			# Three of a kind			
			elif c == 3:
				hv[6] = v
			# Pair or two pair
			elif c == 2:				
				if hv[8] != 0:
					if hv[8] > v:
						hv[7] = hv[8]
						hv[8] = v
					else:
						hv[7] = v
				else:
					hv[8] = v				
		# If full house
		if hv[8] != 0 and hv[6] != 0:
			hv[3] = hv[6]*100 + hv[8]
	
	hv.extend(cards)					
	return hv
  

def comparehands(h):
	p1 = handscore(h[:5])
	p2 = handscore(h[5:])
	return p1 > p2
	
lines = open("054.txt", "r").readlines()
p1wins = 0
p2wins = 0
for l in lines:
	h = l.strip().split()
	if comparehands(h):		
		p1wins += 1
	else:
		p2wins += 1
	
print(p1wins)
print(p2wins)

end = time.time() - start
print ("Total time was " + str(end)+ " seconds")
    
