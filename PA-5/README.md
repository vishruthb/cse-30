# Programming Assignment #5

## Problem A

### Background:
A binary search tree (BST), also called an ordered or sorted binary tree, is a rooted binary tree data structure with the key of each internal node being greater than all the keys in the respective node's left subtree and less than the ones in its right subtree. Binary search trees allow binary search for fast lookup, addition, and removal of data items. Since the nodes in a BST are laid out so that each comparison skips about half of the remaining tree, the lookup performance is proportional to that of binary logarithm (when the tree is balanced).

### Problem Statement:
You need to implement a function that takes three arguments: 

* tree: the root of BST,  (all the elements in the tree are integers)
* f: a float value F
* p: an integer P

The function should return the P closest values to the value F in the BST. You may return the answer in any order. You are guaranteed to have only one unique set of P values in the BST that are closest to F. Below is an example for the BST class, which is also included in the template files under Programming Assignment 5 in the files section

```python
class BinarySearchTree:

    def __init__(self, val: int, left: 'Union[BinarySearchTree, None]'=None, right: 'Union[BinarySearchTree, None]'=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        #this is a helper function which returns the BST as a string
        return '{} [{}] [{}]'.format(self.val, self.left, self.right)

  
def get_closest_numbers(tree: BinarySearchTree, f: float, p: int) -> 'List[int]':
    p_closest_numbers=[]
    # your code

    return p_closest_numbers
```
 #### Examples:
 * Example 1:
 
Inputs: ``` Root node 5, F: 4.82, P = 2 ```

Output: ``` python [ 5, 4 ] ```
