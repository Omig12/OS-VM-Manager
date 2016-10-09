 # Israel O. Dilan Pantojas
 # 801-11-2035
 # First in First Out Replacement

import sys
import string
# Notation R:5 (Read Page 5), w:5 (Write Page 5)

# python optimal.py <Number of physical memory pages> <access sequence file>

NPMP = int(sys.argv[1])
ASF  = sys.argv[2]
pages = []
pos = 0

f = open(ASF,'r')

jobs = f.read()
jobs = jobs.strip()
jobs = jobs.split(" ")
f.close()

# print jobs
# print NPMP

for i in jobs:
	if (len(pages) < NPMP):
		if (i.split(":")[1] in pages):
			print "Page Hit"
		else:
			pages.append(i.split(":")[1])
			print "Page Fault", pages
	else:
		if i.split(":")[1] in pages:
			print "Page Hit"
		else:
			print "Page Fault" 
			if (pos < len(pages)-1):
				pages[pos] = i.split(":")[1]
				pos += 1
			else:
				pages[pos] = i.split(":")[1]
				pos = 0
		print pages