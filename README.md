# README.md
### Israel O. Dilan Pantojas
### 801-11-2035

What is OS_VM_Manager?
______________________

It is a set of python code that aims to simulate the workings of an operating systems 
Memory Manager. It presents the changes that happen when updating a simple 
representation of a page table and have to swap out different pages. This is done 
implementing diferent algorithms, such as:
+ *First In First Out Replacement*
+ *Optimal Replacement*
+ *Sencond Chance Replacement*
+ *Working Set Clock Replacement*

Important:
----------
Te notation for all input files is as follows:
> Notation R:5 (Read Page 5), w:5 (Write Page 5)

`R:1 R:3 W:2 R:2 R:1 ...`

## First In First Out Replacement
----------------------------------------------------------------------------

The first in first out replacement algorithm works by first replacing the 
oldest page within the table and then moving up to the second oldest and so 
forth.

**_To run:_**
```sh 
$ python fifo.py <Number of physical memory pages> <access sequence file>
```

**_Example:_**
```python
R:1 W:1 W:2 R:3 R:1 R:4 W:5 R:2 R:2 R:2 W:2 W:3 R:2
Page Table: [5,4,2]
Table size: 3
Page Faults: 7
Page Hits: 6
```
## Optimal Replacement
----------------------------------------------------------------------------

The optimal replacement algorithm works by replacing the page that will be  
references again the latest from all al the pages currently in the table look
aside buffer.

**_To run:_**
```sh 
$ python optimal.py <Number of physical memory pages> <access sequence file>
```

**_Example:_**
```python
R:1 W:1 W:2 R:3 R:1 R:4 W:5 R:2 R:2 R:2 W:2 W:3 R:2

Page table: [3,2,5]
Table size: 3
Page Faults: 6
Page Hits: 7
```

## Second Chance 
----------------------------------------------------------------------------

The second chance replacement algorithm basically works like the fifo 
algorithm the only difference being that it gives each page that is going to 
be removed a second chance to join the queue if it was marked as referenced
when it was removed.  

**_To run:_**
```sh
$ python second.py <Number of physical memory pages> <access sequence file>
```

## Working Set Clock
----------------------------------------------------------------------------

The working set clock algorithm prioratizes time efficiency by keeping track
which pages have been present in the table longer than their working set, 
which pages have been referenced and which pages have been written to or 
modified. Following this three critireon the algorithm can hopefully evict a
less needed (not referenced), clean (not modified) and old page (largest time).

**_To run:_**
```sh
$ python wsclock.py <Number of physical memory pages> <tau> <access sequence file>
```

=============================================================================

## Discussed with:
+ Jeffrey A. Chan
+ Alejandro S. Vega
+ Omar Cruz Pantoja
+ Juan Lugo Torres