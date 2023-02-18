# Programming Assignment 1

## Problem A (6 pts + 1 extra pt)

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
 

## Problem B (6 pts + 1 extra pt)
Write a function that takes two lists as input and returns a list of common elements of the input lists.  You may return the result in any order.

Function Signature
def common_elements(list_1: list, list_2: list) -> list:
Examples
Input	
list_1
[ 2, 5, 4, 1]
list_2
[ 5, 3, 6, 2, 4, 10, 11, 15, 9]
Output		
[ 2, 4, 5 ]
 

Input	
list_1
[ 8, 3, 8, 7, 3]
list_2
[ 3, 8, 4]
Output		
[3,8]
 

What if the size of one of the input lists is way smaller than the other list? Would you solve the problem differently (more efficiently), if so how? Please explain as part of comments (or doc strings) along with any efficient solution (python code) you propose.
