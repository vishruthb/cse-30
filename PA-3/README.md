# Programming Assignment #3
Implement Ring Buffer (using Queues)
Background:
A Ring Buffer (or circular queue or circular buffer), is an extended version of a queue where the last element is connected to the first element, forming a circle-like structure. In this Queue, we can insert elements even the queue becomes full, but once the queue becomes full, the new elements will overwrite the old elements. Ring Buffers use the circular structure to keep the first and last indices dynamic, allowing elements to be enqueued without emptying the whole queue each time.

Reference:  https://en.wikipedia.org/wiki/Circular_bufferLinks to an external site.

 

Problem Statement:
Implement a RingBuffer for a stream of integers with the following features

Initializes the ringBuffer with a maximum size of k.
enqueue() -> None: Adds an item at the rear of the queue. If the queue is full, then remove the front element and place the new value at the back of the queue (sliding window queue).
dequeue() -> boolean: Deletes the item at the front of the queue. otherwise returns False if the operation is not successful.
get_front() -> int: Returns the front item from the queue. Returns -1 if the queue is empty.
get_rear() -> int: Returns the last item from the queue. Returns -1 if the queue is empty.
is_empty() -> boolean: Returns true if the queue is empty, or false otherwise.
is_full() -> boolean: Returns true if the queue is full, or false otherwise.
get_average() -> float: Returns average of numbers in the ringBuffer, if it is empty returns None
Note: it is important that when you enqueue, you update the index of the rear by one, that way the index of rear points to the most recent element. Likewise, when you dequeue, you update the index of the front by one to point at the next item at the front. Modulo operators could help with this

Constraints:

enqueued values will always be integers
All functions should maintain the return type listed above. The example code below also includes the return type after the "->" sign
You may use the starting code below as a starting template for your submission. Please make sure to keep to the naming conventions listed below, even if you do not use the template. Failure to follow naming conventions will fail the autograders and result in a 0 on the assignment

 

class RingBuffer:

     def __init__(self, k: int):

     def en_queue(self, value: int) -> None:

     def de_queue(self) -> bool:

     def get_front(self) -> int:

     def get_rear(self) -> int:

     def is_empty(self) -> bool:

     def is_full(self) -> bool:

     def get_average(self) -> float:  



Comprehensive Example I/O: 

ringBuffer = RingBuffer(3)

ringBuffer.is_empty() # return True

ringBuffer.en_queue(1) # return None (No return is necessary for this function)

ringBuffer.en_queue(2) # return None

ringBuffer.en_queue(3) # return None

ringBuffer.en_queue(4) # return None (the queue is full).  → it should overwrite the old values 

ringBuffer.get_rear()      # return 4

ringBuffer.get_front()     # return 2

ringBuffer.is_full()       # return True

ringBuffer.get_average # return 3.0

ringBuffer.de_queue()   # return True

ringBuffer.is_full()       # return False

ringBuffer.de_queue()   # return True

ringBuffer.de_queue()   # return True

ringBuffer.de_queue()   # return False (queue is empty)

ringBuffer.is_empty()     # return True

ringBuffer.get_rear()      # return -1

ringBuffer.get_front()     # return -1
 

Point Allocation (6 points):
6 points for passing all the test cases for your Circular Queue.

Documentation is necessary ( you should always document your code, even if it's not required! )

 

Submission Instructions:
A single .py file named “ring_buffer.py” containing all of the functions listed above.
Make sure the return types of all functions follow that of the Problem Statement. Returning the wrong type will make grading difficult
As mentioned, please make sure to use the exact name of the file, or you will get a 0 on the assignment. 
Do not include a main function, eval function, or any testing lines in un-commented form, as this may flag the autograder as an error
As always, any questions can be asked either in the Slack channel or one of the TA discussion sections
 

 

 

Evaluate Mathematical Expression (using Stacks)
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero. You may assume that the given expression is always valid. 

Note: You are NOT allowed to use any built-in function, or external library, which evaluates strings as mathematical expressions, such as eval().

Constraints:

s consists of integers and operators  '+', '-', '*', and  '/'  separated by some number of spaces. No other characters and assume the expression is valid
operator precedence 
-, +, *, /   (low to high) (note: this is slightly different from math; - and + are NOT in the same level; so do * and /)
s represents a valid expression. All the integers in the expression are non-negative integers in the range [0, 2^31 - 1].
Point Allocation:

6 points for passing all test cases.

( you should always document your code, even if it's not required! )

 

Submission Instructions:

A single .py file named “ evaluate_expression.py” containing all of the functions listed above.
Make sure the return types of all functions follow that of the Problem Statement. Returning the wrong type will make grading difficult
As mentioned, please make sure to use the exact name of the file, or you will get a 0 on the assignment.
 

You may use the starting code below as a starting template for your submission. Please make sure to keep to the naming conventions listed below, even if you do not use the template. Failure to follow naming conventions will fail the autograders and result in a 0 on the assignment. The autograder will also check the stack implementation in your code. 

 

class EvalExpression:


  def evaluate(self, s: str) -> int:

   '''

    - Parameters:

       - s : expression to be evaluated

    - Returns:

       - int : result of the expression

  

   Iterate through the expression and calculate the expression using stacks.

   '''

   # Your code here


 

Example 1:

Input: s = "3+2*2"

Output: 7

 

Input: s = " 3/2 "

Output: 1

 

Input: s = " 3+5 / 2 "

Output: 5

 

Input: s = " 23 + 4 / 2 "

Output: 25

 

Input: s = " 1000 - 400 / 2 "

Output:  800

 

Reference: Expression evaluation using Stack

https://runestone.academy/ns/books/published/pythonds/BasicDS/InfixPrefixandPostfixExpressions.htmlLinks to an external site.
