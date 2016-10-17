 # Israel O. Dilan Pantojas
 # 801-11-2035
 # Second Chance Replacement

import sys
import string

# Notation R:5 (Read Page 5), w:5 (Write Page 5)

# python second.py <Number of physical memory pages> <access sequence file>

NPMP = int(sys.argv[1]) # Ammount of page frames
ASF  = sys.argv[2]      # Access sequence file "ej: input.txt"
pages = []				# Page table
referenced = {}         # Order access 
pf = 0					# Page fault counter
ph = 0					# Page hit counter
pos = 0

f = open(ASF,'r')

jobs = f.read()
jobs = jobs.strip()
jobs = jobs.split(" ")
f.close()

# print jobs
# print NPMP


# State A1: Physical memory pages < MaxSize
	# Fill array with items/page faults 
# State A2: Physical memory pages = MaxSize
	# Move to B states

# State B1: Looking at first page
# State B2: If not referenced evict
# State B3: If referenced, unreference and move to the back 


# For each page job
for i in jobs:
	value = i.split(":")[1]
	
	# If TLB not full 
	if (len(pages) < NPMP):
	
			# If page already in TLB
			if value in pages:
				referenced[value] = 1
				print "Page Hit  ", pages
				ph += 1

			# If page not in TLB
			else:
				pages.append(value)
				referenced[value] = 1
				print "Page Fault", pages
				pf += 1
	
	#If TLB full
	else:

		# If page already in TLB
		if value in pages:
				referenced[value] = 1
				print "Page Hit  ", pages
				ph += 1
		
		# If page not in TLB
		else:
			flag = 0
			while (flag == 0):
				# Move through positions in table 
				if (pos < len(pages)):
					# Evict non referenced page
					if (referenced[pages[pos]] == 0):
						pages[pos] = value
						referenced[value] = 1
						print "Page Fault", pages
						pf += 1
						pos += 1
						flag += 1
					else:
						referenced[pages[pos]] = 0
						pos += 1
				else:
					pos = 0				

print "The total ammount of page faults was: {}".format(pf)
print "The total ammount of page hits was: {}".format(ph)