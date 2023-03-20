# Programming Assignment #6

## Problem A

### Background:
In the school curriculum, there is a sequential relationship between courses. One can only take the subsequent courses if have finished the prerequisite courses. In this problem, we constructed a list for the courses and their relationships. Your task is to find out the fastest schedule to complete all given courses and **return the corresponding course schedule (course order)**.

### Problem Statement:
Implement the function called: ```get_order_of_courses(relationships: List[List[str]]) -> List[str]```

Function parameters: 
* ```relationships[i] = [prerequisite_course, next_course]```: the ```prerequisite_course``` has to be taken before the ```next_course```. 
* Return type - ```List[str]```: return a list indicating the course order. Each element in the list should be the name of the course. If there is no way to take all the courses, return ```[]```. See section-Hints for more explanation. 

 #### Examples:
 * Example 1:
 
```python
Input: relations = [[CSE-11,CSE-22],[CSE-22,CSE-33]]
Output: ['CSE-11', 'CSE-22', 'CSE-33']

'''
Explanation:
quarter 1: course CSE-11, 
quarter 2: course CSE-22.
quarter 3: course CSE-33.
'''
```

* Example 2:

```python
Input: relations = [[ART-212,ART-232],[ART-232,HIST194],[HIST194,ART-212]]
Output: []

'''
Explanation: There is no way to finish those courses under given relations.
'''
```

* Example 3:

```python
Input: relations = [[HIST-199,LING-211],[HIST-199,ART-912],[HIST-199,ART-431],[HIST-199,ART-55],[LING-211,LING-777]]
Output: ['HIST-199','LING-211','ART-912','ART-431','ART-55','LING-777']

'''
Explanation:
quarter 1: course HIST-199.
quarter 2: course LING-211, ART-912, ART-431, ART-55.
quarter 3: course LING-777.
'''
```

#### Notes/Assumptions/Hints:
* Topological sorting will be the ideal way to solve this.
* In the output schedule, the order that needs to be followed is that: the ```prerequisite_course``` needs to be saved before the ```next_course```. That is, the ```prerequisite_course``` should have a smaller index in the output list. 
* You can assume that all the courses can only have zero or one prerequisite course.
* For courses that can be taken in the same quarter, the order does not matter. For example, all of the following outputs are correct.
```python
  Input: relations = [[HIST-199,LING-211],[HIST-199,ART-912],[HIST-199,ART-431],[HIST-199,ART-55],[LING-211,LING-777]]
  Output1: ['HIST-199','LING-211','ART-912','ART-431','ART-55','LING-777']
  Output2: ['HIST-199','ART-431','LING-211','ART-912','ART-55','LING-777']
  Output3: ['HIST-199','ART-431','LING-211','ART-55','ART-912','LING-777']
  
  '''
  Explanation:
  HIST-199 should be taken first
  ART-431, LING-211, ART-912, ART-55 can be taken at the same time, so the order of those 4 courses does not matter
  LING-777 should be taken last (after LING-211)
  '''
  ```
* Course schedules interpretation may not be unique, but the minimum required quarters are fixed for each input. For example, in Example 3: there are two interpretations of the schedule, as shown below, but the output for this function is still following the order shown in the previous hint.
```python
  Output: ['HIST-199','LING-211','ART-912','ART-431','ART-55','LING-777']
  
  '''
  Interpretation1:
  quarter 1: course HIST-199.
  quarter 2: course LING-211.
  quarter 3: course ART-912, ART-431, ART-55,LING-777
  
  Interpretation2:
  quarter 1: course HIST-199.
  quarter 2: course LING-211, ART-912, ART-431, ART-55.
  quarter 3: course LING-777.
  '''
  ```
* You can assume that the course name will always be a valid string.

## Problem B

### Problem Statement:
Given a List of English words and an integer K, return the K most frequent words. Meanwhile, you need to convert all the words to lowercase, and ignore the stop words (Stop words are given in the template code).

 #### Examples:
 * Example 1:
 
input: ```['Cat', 'bat', 'and', 'a', 'Rat', 'are', 'singing', 'A', 'bat', 'is', 'not', 'the', 'black', 'caT', 'An', 'elephant', 'a', 'Rat', 'and', 'a', 'cat', 'are', 'walking', 'Bat', 'is', 'black', 'but', 'the', 'cat', 'is', 'white', 'And', 'dog', 'is' 'brown']```

output (when ```k = 2```): ```['cat', 'bat']```

* Example 2:

input: ```['The', 'weather', 'is', 'sunny', 'in', 'SC', 'The', 'weather', 'is', 'cloudy', 'the', 'weather']```

output (when ```k = 2```): ```['weather', 'cloudy']```

#### Notes/Assumptions:
* If two words have the same frequency, the word with the lower alphabetical order comes first
* All words in the list are in string type
* K is always a positive integer
* K is smaller or equal to the number of unique words given in the input
* So you don't need to worry about K being larger than the number of items in your result list
* **ONLY GIVEN EXTERNAL LIBRARIES ARE ALLOWED**

