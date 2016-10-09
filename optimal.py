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
order = []
pos = 0

f = open(ASF,'r')

jobs = f.read()
jobs = jobs.strip()
jobs = jobs.split(" ")
f.close()

# print jobs
# print NPMP

for i in jobs:
	if i.split(":")[1] in referenced: 
		referenced[i.split(":")[1]] += 1
	else:
		referenced[i.split(":")[1]] = 1

# print referenced

for i in referenced.keys():
	order.append((int(i) , referenced[i]))

for m in order:
	for i in range(len(order)-1):
		if (order[i][1] > order[i+1][1]): 
			swap = order[i+1]
			order[i+1] = order[i]
			order[i] = swap

# print order

for i in jobs:
	value = i.split(":")[1]
	if (len(pages) < NPMP):
		if ( value in pages):
			print "Page Hit"
		else:
			pages.append(value)
			print "Page Fault", pages
	else:
		if value in pages:
			print "Page Hit  ", pages
		else:
			# print "Order Map:", order
			for x in order:
				if (str(x[0]) in pages):
					# print "Remove Page: {}".format(x[0])
					# print "Insert Page: {}".format(value)
					pos = pages.index(str(x[0]))
					order.remove(x)
					break
			pages[pos] = value
			print "Page Fault", pages