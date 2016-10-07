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
  + Notation R:5 (Read Page 5), w:5 (Write Page 5)

> R:1 R:3 W:2 R:2 R:1 ...



## Optimal Replacement
============================================================================

The optimal replacement algorithm works by replace the page with fewer 
references first and the moving up from least referenced to most referenced.



#####To run: 
"$ python optimal.py <Number of physical memory pages> <access sequence file>"

Example:
111 235 222 23

Page table: [1,2,3]
page fault counter: 5



## Second Chance 
============================================================================

#####To run:
"$ python second.py <Number of physical memory pages> <access sequence file>"

## Working Set Clock
============================================================================

#####To run:
"$ python wsclock.py <Number of physical memory pages> <access sequence file>"