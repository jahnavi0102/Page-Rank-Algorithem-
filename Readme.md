# Random Surfer Model

 The random surfer model provides a basis for calculating the Page Rank algorithm. The model represents the behavior of Internet users and provides a probability of a random user visiting a webpage. The random surfer model provides a basis for calculating the Page Rank algorithm. The model represents the behavior of Internet users and provides a probability of a random user visiting a webpage.

PR(A) = (1-d) + d(PR(Ti)/C(Ti)) +...+PR(Tn)/C(Tn))

PR(A) is the Page Rank of page A
PR(Ti) is the Page Rank of pages Ti which link to page A,
C(Ti) is the number of outbound links on page Ti 
d is the damping factor which cana be set between 0 and 1 

The rank of a document is given by the rank of those  documents which link to it.
The PR of each page depends  on the PR of the pages pointing to it.
In order to get the PR of those pages , we need to calculate the PR of the pages pointing to them.
When a web page has no outbound links , its PageRank cannot be distributed to other pages.
Lawrence Page and Sergey Brin characterise links to those pages as dangling links.


## Implementation of the PageRank Algorithm 

Install numpy using pip install numpy 
   It is basically used for doing heavy calculations of more than one dimension.
Install csv using pip install python-csv 
   It is used for reading a file.

## Data set 

   "hollins.dat" is the data set used for the implementation of the algorithm.      


## PageRank function

  It is called for the calculation of the rank by the particular no. of iterations.  

## Output 
  
  The output of this code is in the "total_rank.txt" file , given in the folder.