 # Israel O. Dilan Pantojas
 # 801-11-2035
 # Optimal Replacement

"""
Algorithm description:

	On each page fault the optimal replacement algorithm measures the distance
	between the pages currently in the page table and their next calls and then
	removes the page that is and

"""

import sys
import string

# Notation R:5 (Read Page 5), w:5 (Write Page 5)

# python optimal.py <Number of physical memory pages> <access sequence file>

NPMP = int(sys.argv[1]) # Ammount of page frames
ASF  = sys.argv[2]      # Access sequence file "ej: input.txt"
pages = []				# Page table
order = []              # Order access 
pf = 0					# Page fault counter
ph = 0					# Page hit counter

f = open(ASF,'r')

jobs = f.read()
jobs = jobs.strip()
jobs = jobs.split(" ")
f.close()


# print jobs
# print NPMP


# List all Accesses
for i in jobs:
	order.append(i.split(":")[1])
print order

# Iterate Acesses
for i in jobs:
	value = i.split(":")[1]
	# Set size of page table
	if (len(pages) < NPMP):
		# If page present page hit
		if (value in pages):
			print "Page Hit  ", pages
			ph += 1
			order.pop(0)
		# If not page fault and insert
		else:
			pages.append(value)
			print "Page Fault", pages
			pf += 1
			order.pop(0)
	# If page table full 
	else:
		# If value already in table 
		if (value in pages):
			print "Page Hit  ", pages
			ph += 1
			order.pop(0)
		# If value not in table
		else:
			# print "Order: ", order
			referenced = {} 		# Next time reference
			flag = 0
			# For each element inside the table
			for x in pages:
				# If item will be accessed again
				if x in order:
					referenced[x] = order.index(x)
					# print referenced
				# If item won't be accessed
				else:
					pages[pages.index(x)] = value
					print "Page Fault", pages
					pf += 1
					order.pop(0)
					flag = 1
					break
			if (len(order) > 1 & flag == 0):
				# print "referenced: " , referenced					
				r = str(max(referenced, key=referenced.get))
				pages[pages.index(r)] = value
				print "Page Fault", pages
				pf += 1
				order.pop(0)
					


print "The total ammount of page faults was: {}".format(pf)
print "The total ammount of page hits was: {}".format(ph)
