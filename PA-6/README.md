# Programming Assignment #6

## Problem A: Get the Order of Courses

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

## Problem B: Find all Paths between Cities

### Background:
We represent the connection between cities using a DAG (directed acyclic graph). The vertex on the graph denotes the city, and the edge denotes the path between cities. Your task is to find out all the path combinations to travel from one given city to another. 

### Problem Statement:
Implement the function called: ```find_paths(connection: List[List[int]], source: int, destination: int) -> List[List[int]]```, to return a list including all paths from the city source to the city destination. You may return them in any order. If the path does not exist, return an empty list. Note that we use the number (```int```) as the name of the city.

##### Function parameters:

* ```connection```: a list with length N, where N is the number of paths involved in this connection map. Each sublist in ```connection```, ```connection[i]=[u,v]```, indicates that there is a path from the city ```u``` to city ```v```.
* ```source```: an integer that represents the name of the city.
* ```destination```: an integer that represents the name of the city.

##### Return :

* ```List[List[int]]```:  a List stores all paths from city source to city destination. Each path should be represented as a list of the city name. 

 #### Examples:
 * Example 1:
 
```python
Input:
  connection = [[0,1],[0,4],[1,2],[2,3],[3,4]]
  source = 2
  destination = 1
Output:
  []

'''
Explanation:
  There is no path connection from city 2 to city 1
  '''
```

* Example 2:

```python
Input:
  connection = [[0,1],[1,2],[1,3],[1,5],[2,3],[2,4],[3,4],[4,5],[0,5]]
  source = 1
  destination = 5
Output:
   [[1,2,3,4,5], [1,2,4,5], [1,3,4,5], [1,5]]
   
'''
Explanation:
  three paths: 1 -> 2 -> 3 -> 4 -> 5 and 1 -> 2 -> 4 -> 5 and 1 -> 3 -> 4 -> 5 and 1 -> 5
  '''
 ```

#### Constraints/Hints:
* Input ```source``` and ```destination``` are different numbers, i.e., ```source ≠ destination```
* Input ```source``` and ```destination``` can always be found in the given connection map
* All cities (vertices) in the connection map are unique
* The ```connection``` is a DAG, i.e., **directed and acyclic**.
* The input connection is not sorted.

## Problem C: Largest Score Pattern (Optional)

### Background:
Given three arrays of the same length: ```username```, ```website```, and ```timestamp```, where each tuple i represents that the user ```username[i]``` visited the website ```website[i]``` at the time ```timestamp[i]```. A pattern is a list of three websites, not necessarily distinct. The score of a pattern is the number of users that consecutive visited all the websites in the pattern in the same order they appeared in the pattern (see more explanation in section:Hints). The task is to find the pattern with the largest score, and if there are multiple patterns with the same score, return the lexicographically smallest pattern.

### Problem Statement:
The task is to implement a function ```find_largest_pattern(username: List[str], timestamp: List[int], website: List[str]) -> List[str]:``` that takes three arrays of strings ```username```, ```website```, and an array of integers ```timestamp```, and returns a list of three strings, representing the pattern with the largest score.

##### Function parameters: 
* ```username```: a list of strings representing the usernames of the users who visited the websites.
* ```timestamp```: a list of integers representing the timestamps at which the users visited the websites.
* ```website```: a list of strings representing the names of the websites visited by the users.

##### Return :
* List[str]: a list of three strings representing the website pattern with the largest score.

#### Examples:
 * Example 1:
 
```python
Input:
  username = ["bob","bob","bob","john","john","john","john","mike","mike","mike"],
  timestamp = [1,2,3,4,5,6,7,8,9,10], 
  website = ["song","page","faq","song","cart","maps","song","song","page","faq"]

Output:
  ["song","page","faq"]

'''
Explanation:
  The tuples in this example are:
  ["bob","song",1],["bob","page",2],["bob","faq",3],["john","song",4],
  ["john","cart",5],["john","maps",6],["john","song",7],["mike","song",8],["mike","page",9], and ["mike","faq",10].

  The pattern ["song", "page", "faq"] has score 2 (bob and mike).
  The pattern ["song", "cart", "maps"] has score 1 (john).
  The pattern ["cart", "maps", "song"] has score 1 (john).
  The pattern ["song", "cart", "song"] has score 0 (john visited "maps" in-between "song" and "cart").
  The pattern ["song", "maps", "song"] has score 0 (john visited "cart" in-between "song" and "maps").
  The pattern ["song", "song", "song"] has score 0 (no user visited song 3 times).
'''
```

#### Notes/Assumptions/Hints:
* It is guaranteed that there is at least one valid pattern in the input
* You can assume that given lists are always sorted by the timestamp 
* The websites in the pattern must be visited by a user continuously (user-wise) for a score. For example, John visited ["song","cart","maps","song"]; then, we cannot say ["song","maps","song"] is a visited pattern of John, since John also visited "cart" in-between "song" and "maps".
Continuous visits are defined user-wise. For example, John visited ["song","cart","maps","song"] at timestamp [1,2,3,5], and another user Bob visited ["cart"] at timestamp [4]. This will not break the continuity of pattern ["cart","maps","song"]
* This problem is not closely related to graph theory. Think of it more in terms of OTHER data structures
