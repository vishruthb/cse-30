<h1> Programming Assignment #4 </h1> 

## Problem A - Recursion on Single Linked List

### Problem Statement:
This problem is about single-linked lists. You are given the heads of two sorted linked lists:  linked_list_1 and linked_list_2, containing only integer values and ending with None. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list. You must solve this problem using recursion.

#### Examples

* Example 1
```python
linked_list_1: 1 -> 3 -> 5 -> None
linked_list_2: 2 -> 4 -> 6 -> None
```
```python
output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
```
* Example 2
```python
linked_list_1: None
linked_list_2: None
```
```python
output: None
```
* Example 3
```python
linked_list_1: 5 -> None
linked_list_2: 2 -> 4 -> 6 -> None
```
```python
output: 2 -> 4 -> 5 -> 6 -> None
```
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
* Example 3
```python
 in_dict:
{
    'a': 2,
    'b': {'x': 2},
    'c': {'p': {'h': 2, 'r': 5}},
}
```
```python
output: 11
```
* Example 4
```python
in_dict: 
{
    'a': 2,
    'b': {'x': 2, 'y': {'foo': 3, 'z': {'bar': 2}}},
    'c': {'p': {'h': 2, 'r': 5}, 'q': 'ball', 'r': 5},
    'd': 1,
    'e': {'nn': {'lil': 2}, 'mm': 'car'}
}
```
```python
output: 24
```
**EXTERNAL LIBRARIES SHOULD NOT BE USED**
