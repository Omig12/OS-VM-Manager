 # Israel O. Dilan Pantojas
 # 801-11-2035
 # Working set clock Replacement

import sys
import string

# Notation R:5 (Read Page 5), w:5 (Write Page 5)

# python wsclock.py <Number of physical memory pages> <tau> <access sequence file>

NPMP = int(sys.argv[1])
TAU  = sys.argv[2]
ASF  = sys.argv[3]
pages = []
pos = 0

class pageClass:
	"""Page Class"""
	def __init__(self, dir, ref, ) :
		self.dir = dir
		self.ref = ref
		self.mod = mod

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


print "The total ammount of page faults was: {}".format(pf)
print "The total ammount of page hits was: {}".format(ph)