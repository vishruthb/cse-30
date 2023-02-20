# -*- coding: utf-8 -*-
"""
# Programming Assignment 4, Problem B, CSE30-02, Winter 2023

## README

* Please **carefully** follow the instructions given in this template
  code
* Only edit within the allowed sections as instructed by the
  comments; you are risking your own assignment grade if you make
  edits outside those sections or deviate from the instructions
* The testing script provided at the end only performs some basic
  tests; it DOES NOT imply anything about your assignment grade
  * You may add your own tesing code in the main function while working
    on your assignment
  * **However**, you will need to remove your own testing code, and
    re-run the original testing script right before you submit the
    code, to ensure your code is free from syntax errors
"""

#===== Import section begins
# In this assignment, external libraries are NOT allowed
# DO NOT ADD any import statements
# keep this section as is
#===== Import section ends


#===== Helper classes/functions section begins
# You may add your own classes or functions within this section
# **class** and **function** only!
# any statement that is not encapsulated inside a class or function
# may result in 0 grade

#===== Helper classes/functions section ends


#===== Problem B function begins
# follow the instruction below
# DO NOT change the function signature!

def nested_dict_sum(in_dict: 'Union[int, str, dict]') -> int:
    '''
    Sum of all the positive integers in a dictionary
    - Parameters:
        - in_dict: the input, which can either be a int, a str, or a dict
    - Returns:
        - int: Sum of all the positive integers in a dictionary
    '''
    #===== Your implementation begins here

    # If in_dict is an int, then return it
    if type(in_dict) is int:
      return in_dict
    
    # If in_dict is a str, then return 0
    elif type(in_dict) is str:
      return 0

    # If in_dict is a dictionary, then iterate through its items
    elif type(in_dict) is dict:
      dsum = 0
      for i,j in in_dict.items():

          # If the value is a dictionary, then recursively call the function
          if isinstance(j, dict):
              dsum += nested_dict_sum(j)

          # If the value is an integer, add its value to the sum
          elif isinstance(j, int):
              dsum += j

      # Return the sum of all positive integers in in_dict
      return dsum

    #===== Your implementation ends here
    pass

#===== Problem B function ends


#===== Testing scripts main function section begins
# follow the instruction below
# DO NOT add any statement outside of main() function
def main() -> None:
    # you may add your own testing code within this function while you're
    # working on your assignment;
    # however, please remember to remove them, and re-run this testing script
    # right before you submit your work, in order to ensure your code is
    # free from syntax error

    dict_1 = 2
    res_1 = 2

    dict_2 = 'foo'
    res_2 = 0

    dict_3 = {
        'a': 2,
        'b': {'x': 2},
        'c': {'p': {'h': 2, 'r': 5}},
    }
    res_3 = 11

    dict_4 = {
        'a': 2,
        'b': {'x': 2, 'y': {'foo': 3, 'z': {'bar': 2}}},
        'c': {'p': {'h': 2, 'r': 5}, 'q': 'ball', 'r': 5},
        'd': 1,
        'e': {'nn': {'lil': 2}, 'mm': 'car'}
    }
    res_4 = 24

    print('Test case 1')
    out_res = nested_dict_sum(dict_1)
    print('Dictionary:      ', dict_1)
    print('Expected result: ', res_1)
    print('Your result:     ', out_res)
    type_match = type(res_1) == type(out_res)
    type_match_str = '==' if type_match else '!='
    print('Return Type:     ', 'type(Expected result)', type_match_str, 'type(Your result)')
    print()

    print('Test case 2')
    out_res = nested_dict_sum(dict_2)
    print('Dictionary:      ', dict_2)
    print('Expected result: ', res_2)
    print('Your result:     ', out_res)
    type_match = type(res_2) == type(out_res)
    type_match_str = '==' if type_match else '!='
    print('Return Type:     ', 'type(Expected result)', type_match_str, 'type(Your result)')
    print()

    print('Test case 3')
    out_res = nested_dict_sum(dict_3)
    print('Dictionary:      ', dict_3)
    print('Expected result: ', res_3)
    print('Your result:     ', out_res)
    type_match = type(res_3) == type(out_res)
    type_match_str = '==' if type_match else '!='
    print('Return Type:     ', 'type(Expected result)', type_match_str, 'type(Your result)')
    print()

    print('Test case 4')
    out_res = nested_dict_sum(dict_4)
    print('Dictionary:      ', dict_4)
    print('Expected result: ', res_4)
    print('Your result:     ', out_res)
    type_match = type(res_4) == type(out_res)
    type_match_str = '==' if type_match else '!='
    print('Return Type:     ', 'type(Expected result)', type_match_str, 'type(Your result)')
    print()


if __name__ == '__main__':
    main()

#===== Testing scripts main function section ends