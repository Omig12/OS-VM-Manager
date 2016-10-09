 # Israel O. Dilan Pantojas
 # 801-11-2035
 # Second Chance Replacement

import sys
import string

# Notation R:5 (Read Page 5), w:5 (Write Page 5)

# python second.py <Number of physical memory pages> <access sequence file>

NPMP = int(sys.argv[1])
ASF  = sys.argv[2]
pos = 0
pages = []


f = open(ASF,'r')

jobs = f.read()
jobs = jobs.strip()
jobs = jobs.split(" ")
f.close()

# print jobs
# print NPMP


for i in jobs:
	value = i.split(":")[1]
	if (len(pages) == 0):
		pages.append((value, 0))
		print "Page Fault", pages
	elif (len(pages) < NPMP):
		for x in pages:
			if (value == str(x[0])):
				tmp = pages.index(x)
				pages[tmp] = (str(x[0]), 1) 
				print "Page Hit"
			else:
				pages.append((value, 0))
				print "Page Fault", pages
	else:
		for x in pages:
			if (pos < len(pages)-1):
				if (str(value) == str(x[0])):
					tmp = pages.index(x)
				 	pages[tmp] = (str(x[0]), 1)  
					print "Page Hit"
					pos += 1
			else:
				if (str(value) == str(x[0])):
					tmp = pages.index(x)
				 	pages[tmp] = (str(x[0]), 1)  
					print "Page Hit"
				else:
					pages[pos] = (value, 0)
				pos = 0
			print "Page Fault", pages