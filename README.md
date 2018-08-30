# Number-of-ways-to-Partition-a-set
Solved the problem of "Given a set of n elements, find number of ways of partitioning it" using algorithm derived from 
Genetic Algorithms and the power of python 3 itertools. 

Main idea is to generate all the unique 1 way, 2 way, ..., (n-1) way unique combinations from the given data. 

when n=3, we will have the following unique combinations.

[('r1',), ('r2',), ('r3',)], [('r1', 'r2'), ('r1', 'r3'), ('r2', 'r3')], [('r1', 'r2', 'r3')]

Pop the last guy, as its already 1 way to parition a set.

[('r1',), ('r2',), ('r3',)], [('r1', 'r2'), ('r1', 'r3'), ('r2', 'r3')]]

Now find all the 2 way..., n way combinations among the above tuples and remove all combinations where any of the records
reoccur

You will find combinations like
[(('r1',), ('r2',)),
  (('r1',), ('r3',)),
  (('r1',), ('r1', 'r2')),
  (('r1',), ('r1', 'r3')),
  (('r1',), ('r2', 'r3')),
  (('r2',), ('r3',)),
  (('r2',), ('r1', 'r2')),
  (('r2',), ('r1', 'r3')),
  (('r2',), ('r2', 'r3')),
  
remove combinations like  (('r1',), ('r1', 'r2')), where a record reoccurs. and at the end you will be left with the solution

Total number of possible clustering arrangements is  5

Clustering arrangements with  1  cluster:

No. of clustering arrangements: 1
The clusters are:
('r1', 'r2', 'r3')

Clustering arrangements with  2  cluster:
No. of clustering arrangements:  3
The clusters are:
[(('r1',), ('r2', 'r3')), (('r2',), ('r1', 'r3')), (('r3',), ('r1', 'r2'))]

Clustering arrangements with  3  cluster:
No. of clustering arrangements:  1
The clusters are:
(('r1',), ('r2',), ('r3',))

Its based on Genetic Algo , because 1st we create the combinations which are our parents, then we commit these parents to
mate via combinations again and the pass them through a fitness function which checks for duplicate records.
Mutation is not required as we already have all the possible parents. And there is no need to run these though n iterations.
