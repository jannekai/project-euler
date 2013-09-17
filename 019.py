import time
import math
import sys

start = time.time()

months      = dict()
months[1]   = 31
months[2]   = 28
months[3]   = 31
months[4]   = 30
months[5]   = 31
months[6]   = 30
months[7]   = 31
months[8]   = 31
months[9]   = 30
months[10]  = 31
months[11]  = 30
months[12]  = 31

year        = 1900
month       = 1
day         = 1
weekDay     = 1
monthDays   = 0
sundays		= 0
isLeap      = False

while year < 2001:
	month  = 1
	isLeap = False
	if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
		isLeap = True
		
	while month <= 12:        
		day = 1
		monthDays = months[month]
		if isLeap and month == 2:
			monthDays = 29        				

		while day <= monthDays:
			if day == 1 and weekDay == 7 and year > 1900:
				sundays += 1
				print (year, month, day, sundays)					
			weekDay += 1
			if weekDay > 7:
				weekDay = 1				
			day += 1        
		month += 1
	year += 1

print sundays

end = time.time() - start
print "Total time was " + str(end)+ " seconds"
