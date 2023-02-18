Problem A (6 pts + 1 extra pt)
A 2-dimensional grid (or nested list) of 0s and 1s sorted in non-increasing  (descending order -- largest to smallest) order both row-wise and column-wise. Write a function that takes the grid as an input and returns the number of zeros in the grid. Assume that each list in the nested list has the same length (as in matrices).

Function Signature
def num_of_zeros(grid: list) -> int:
Examples
Input	
grid
[[1,1,1,0],[1,1,1,0],[1,1,0,0],[0,0,0,0]]
Output		
8
 

Input	
grid
[[1, 1],[1, 1]]
Output		
0
