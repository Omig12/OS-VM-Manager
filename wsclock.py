 # Israel O. Dilan Pantojas
 # 801-11-2035
 # Working set clock Replacement

"""
	The working set clock algorithm tries to create a favorable scenario
	to evict old, unused and non-modified pages. 
	
	Best case: 
		There is an old, unused, unmodified page to evict.
		Solution:
			Evict Page

	Cases:
		There is an old, referenced, unmodified page.
		Solution:
			Unreference, give second chance but evict if no other candidate is found. 

		There is an old, unused, modified page.
		Solution:
			Schedual for write, move hand. 

		There is an old, used, modified page.
		Solution:
			Unreference, schedual for write and move hand.

		All pages are old, used and modified.
		Solution:
			Unreference, schedual for write and wait for one to finish.

	Worst Case:
		There is no old pages to evict.
		Solution:
			Evict Random page, prefferably one Non-Referenced or Non-modified.

"""


import sys
import string
import random 

# Notation R:5 (Read Page 5), w:5 (Write Page 5)

# python wsclock.py <Number of physical memory pages> <tau> <access sequence file>

NPMP = int(sys.argv[1]) # Ammount of page frames
TAU  = int(sys.argv[2]) # Life of a working set
ASF  = sys.argv[3]      # Access sequence file "ej: input.txt"
pages = []              # Page table
clock = 0               # Current Virtual Time 
hand = 0                # Hand that points to the page to inspect
tolu = {}				# Time of last use			
referenced = {}         # Referenced bit
modified = {} 			# Modified bit
writting = []			# Writting operations 
pf = 0                  # Page fault counter
ph = 0					# Page hit counter

# class pageClass:
# 	"""Page Class"""
# 	def __init__(self, dir, ref, mod) :
# 		self.p = p
# 		self.r = r 
# 		self.m = m
# 		self.c = c

f = open(ASF,'r')
jobs = f.read()
jobs = jobs.strip()
jobs = jobs.split(" ")
f.close()


# print jobs
# print NPMP


# State A1: Physical memory pages < MaxSize
	# Fill array with item
# State A2: Physical memory pages = MaxSize
	# Move to B states

# State B1: If non referenced, non modified and old 
	# Evict page
	# Advance hand
# State B2: If non referenced and old evict, but modified 
	# Unreference and Schedule Write job
	# Advance Hand
# State B3: If there are no old pages in table    
	# Evict Random Page 
 

# For each page job
for i in jobs:

	# Parse job
	value = i.split(":")[1]

	# Update the clock of each page
	clock += 1

	# If Page Table not full 
	if (len(pages) < NPMP):
	
			# If page already in Page Table
			if value in pages:
				referenced[value] = 1
				tolu[value] = clock
				print "Page Hit  ", pages
				ph += 1

			# If page not in Page Table
			else:
				pages.append(value)
				referenced[value] = 0
				tolu[value] = clock 
				# If page is modified mark as dirty
				if i.split(":")[0] == "W":
					modified[value] = 1
				else:
					modified[value] = 0
				print "Page Fault", pages
				pf += 1
	
	#If Page Table full
	else:

		# If page already in Page Table
		if value in pages:
				referenced[value] = 1
				tolu[value] = clock
				print "Page Hit  ", pages
				ph += 1
		
		# If page not in Page table
		else:
			flag = 0
			rounds = 0
			while (flag == 0):
		
				# Move through positions in table 
				if (hand < len(pages)):

					# No valid page found on pass two of the clock
					if rounds == 3:
						# Random old page finishes writting to disk 
						t = random.randint(0, len(writting)-1)
						finished = writting[t]
						modified[finished] = 0

					# No page older than working set
					if rounds > 3:
						# Evict Random non referenced, non modified Page, not older than tau page
						if (referenced[pages[hand]] == 0 and modified[pages[hand]] == 0):
							modified[pages[hand]] = 0
							pages[hand] = value
							referenced[value] = 0
							# If page is modified mark as dirty
							if i.split(":")[0] == "W":
								modified[value] = 1
							else:
								modified[value] = 0
							tolu[value] = clock
							print "Page Fault", pages
							pf += 1
							hand += 1
							flag += 1
						else:
							hand += 1
							rounds += 1	

					# Evict non referenced page, non modifies old page
					if (referenced[pages[hand]] == 0 and tolu[pages[hand]] > (clock - TAU) and modified[pages[hand]] == 0 and rounds <= 3):
						modified[pages[hand]] = 0
						pages[hand] = value
						referenced[value] = 0
						# If page is modified mark as dirty
						if i.split(":")[0] == "W":
							modified[value] = 1
						else:
							modified[value] = 0

						tolu[value] = clock
						print "Page Fault", pages
						pf += 1
						hand += 1
						flag += 1
					
					# If non referenced and old but modified schedule a write job
					elif (referenced[pages[hand]] == 0 and tolu[pages[hand]] > (clock - TAU) and modified[pages[hand]] == 1 and rounds <= 3):
						referenced[pages[hand]] = 0
						writting.append(pages[hand])
						hand += 1
					# Set reference bit to 0
					else:
						referenced[pages[hand]] = 0
						hand += 1
				else:
					hand = 0
					rounds += 1	

print "The total ammount of page faults was: {}".format(pf)
print "The total ammount of page hits was: {}".format(ph)