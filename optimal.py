 # Israel O. Dilan Pantojas
 # 801-11-2035
 # Optimal Replacement

import sys
import string
# Notation R:5 (Read Page 5), w:5 (Write Page 5)

# python optimal.py <Number of physical memory pages> <access sequence file>

NPMP = int(sys.argv[1])
ASF  = sys.argv[2]
pages = []
referenced = {}


f = open(ASF,'r')

jobs = f.read()
jobs = jobs.strip()
jobs = jobs.split(" ")

# print jobs
# print NPMP

for i in jobs:
	if (len(pages) < NPMP):
		pages.append(i.split(":")[1])
		print "Page Fault", pages
	if i not in referenced:
		referenced[i.split(":")[1]] += 1
	else:
		for x in range(len(pages)):
			if (x < len(pages)-1):
				pages[int(x)] = pages[int(x)+1]
			else:
				pages[len(pages)-1] = i.split(":")[1]
		print pages