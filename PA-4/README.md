# Programming Assignment #4

## Problem A - Recursion on Single Linked List

### Problem Statement:
This problem is about single-linked lists. You are given the heads of two sorted linked lists:  linked_list_1 and linked_list_2, containing only integer values and ending with None. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list. You must solve this problem using recursion.

#### Examples

* Example 1

linked_list_1: 1 -> 3 -> 5 -> None
linked_list_2: 2 -> 4 -> 6 -> None
output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

* Example 2

linked_list_1: None

linked_list_2: None

output: None

* Example 3

linked_list_1: 5 -> None

linked_list_2: 2 -> 4 -> 6 -> None

output: 2 -> 4 -> 5 -> 6 -> None

**EXTERNAL LIBRARIES SHOULD NOT BE USED**

## Problem B - Recursion on Nested Dictionary

### Problem Statement:

Write a recursive function that will return the sum of all the integer numbers in a dictionary which may contain more dictionaries nested in it. You must solve this problem using recursion.

#### Examples
* Example 1
```python
in_dict: 2
```
```python
output: 2
```
* Example 2
```python
in_dict: 'foo'
```
```python
output: 0
```
Example 3
 in_dict:
{
    'a': 2,
    'b': {'x': 2},
    'c': {'p': {'h': 2, 'r': 5}},
}
output: 11
Example 4
in_dict: 
{
    'a': 2,
    'b': {'x': 2, 'y': {'foo': 3, 'z': {'bar': 2}}},
    'c': {'p': {'h': 2, 'r': 5}, 'q': 'ball', 'r': 5},
    'd': 1,
    'e': {'nn': {'lil': 2}, 'mm': 'car'}
}
output: 24
Please patiently read through and follow the instructions below and the instructions in the template file; otherwise, any violation of these instructions may result in 0 points in this problem
You should use the provided template python file to begin your work
the template file can be found in File -> ProgrammingAssignment-4 -> nested_dict_sum.py
alternatively, you may use the colab notebook version, under the File -> ProgrammingAssignment-4 -> Colab Notebook Version directory. But, after you finish your work, please download the notebook as a python file (NOT a notebook file)
on the menu bar (Colab's menu bar, NOT your browser's menu bar), go to File -> Download -> Download .py
you are expected to download the template file from Canvas, follow the instructions in that file, work directly in that file, and turn the entire python file in
Notes:
You may assume:
All the integers in the dictionary are positive integers
All keys in the dictionary are in string type
The value in the dictionary could either be an integer, a string, or a nested dictionary
for values in string type, you may ignore them, or treat them as 0
You must use recursion to solve the problem
The function `nested_dict_sum` itself must be a recursive function
Recursive function (programming), a function which references itself - source: wikipediaLinks to an external site.
If you didn't use recursion, or  `nested_dict_sum` is not a recursive function, no points will be given
EXTERNAL LIBRARIES SHOULD NOT BE USED
Point Allocation (6 points):
6 points for passing all the test cases
Documentation is necessary ( you should always document your code, even if it's not required! )
Submission Instructions:
A single python (.py) file named “nested_dict_sum.py”
Please read this announcement and this announcement carefully before submitting your assignment
Do a double-check right before submitting the code, to ensure your code is free from syntax errors and aligns with ALL given instructions
