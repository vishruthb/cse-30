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
 
inputs: ``` Root node 5, F: 4.82, P = 2 ```

output: ``` [5,4] ```

* Example 2:

inputs: ``` Root node 3, F = 1.20, P = 1 ```

output: ``` [3] ```

* Example 3:

inputs: ``` Root node 8, F = 99.90, P = 4 ```

output: ``` [8,10,13,14] ```

#### Notes/Assumptions:
* There is only one unique set of P values in the BST that are closest to F
* All the elements in the tree are integers
* **EXTERNAL LIBRARIES SHOULD NOT BE USED**


## Problem B

### Problem Statement:
Given a List of English words and an integer K, return the K most frequent words. Meanwhile, you need to convert all the words to lowercase, and ignore the stop words (Stop words are given in the template code).

 #### Examples:
 * Example 1:
 
input: ``` ['Cat', 'bat', 'and', 'a', 'Rat', 'are', 'singing', 'A', 'bat', 'is', 'not', 'the', 'black', 'caT', 'An', 'elephant', 'a', 'Rat', 'and', 'a', 'cat', 'are', 'walking', 'Bat', 'is', 'black', 'but', 'the', 'cat', 'is', 'white', 'And', 'dog', 'is' 'brown']```

output (when ```k = 2 ```): ``` ['cat', 'bat'] ```

* Example 2:

input: ``` ['The', 'weather', 'is', 'sunny', 'in', 'SC', 'The', 'weather', 'is', 'cloudy', 'the', 'weather'] ```

output (when ```k = 2 ```): ``` ['weather', 'cloudy'] ```

#### Notes/Assumptions:
* If two words have the same frequency, the word with the lower alphabetical order comes first
* All words in the list are in string type
* K is always a positive integer
* K is smaller or equal to the number of unique words given in the input
* So you don't need to worry about K being larger than the number of items in your result list
* **ONLY GIVEN EXTERNAL LIBRARIES ARE ALLOWED**

