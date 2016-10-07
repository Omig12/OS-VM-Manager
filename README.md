# README.md
### Israel O. Dilan Pantojas
### 801-11-2035

What is OS_VM_Manager?
======================

It is a set of python code that aims to simulate the workings of an operating systems 
Memory Manager. It presents the changes that happen when updating a simple 
representation of a page table and have to swap out different pages. This is done 
implementing diferent algorithms, such as:
  + First In First Out Replacement
  + Optimal Replacement
  + Sencond Chance Replacement
  + Working Set Clock Replacement




Important:
----------

Te notation for all input files is as follows:
> Notation R:5 (Read Page 5), w:5 (Write Page 5)

`R:1 R:3 W:2 R:2 R:1 ...`

## First In First Out Replacement
============================================================================

The first in first out replacement algorithm works by first replacing the 
oldest page within the table and then moving up to the second oldest and so 
forth.

**_To run:_** 
`$ python fifo.py <Number of physical memory pages> <access sequence file>`

**_Example:_**
`
R:1 W:1 W:2 R:3 R:1 R:4 W:5 R:2 R:2 R:2 W:2 W:3 R:2

Page Table: [5,4,2]
Table size: 3
page Faults: 7
Page Hits: 6
`

## Optimal Replacement
============================================================================

The optimal replacement algorithm works by replace the page with fewer 
references first and the moving up from least referenced to most referenced.

#####To run: 
`$ python optimal.py <Number of physical memory pages> <access sequence file>`

#####Example:
`
R:1 W:1 W:2 R:3 R:1 R:4 W:5 R:2 R:2 R:2 W:2 W:3 R:2

{ID:# of times references}
Reference Table: {1:3, 2:6, 3:2, 4:1, 5:1}

Page table: [4,2,5]
Table size: 3
Page Faults: 6
Page Hits: 7
`


## Second Chance 
============================================================================

#####To run:
`$ python second.py <Number of physical memory pages> <access sequence file>`

## Working Set Clock
============================================================================

#####To run:
`$ python wsclock.py <Number of physical memory pages> <access sequence file>`