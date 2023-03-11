# -*- coding: utf-8 -*-
"""
# Programming Assignment 5, Problem B, CSE30-02, Winter 2023

## README

* Please **carefully** follow the instructions given in this template
  code
* Only edit within the allowed sections as instructed by the
  comments; you are risking your own assignment grade if you make
  edits outside those sections or deviate from the instructions
* The testing script provided at the end only performs some basic
  tests; **it DOES NOT imply anything about your assignment grade**
  * You may add your own tesing code in the main function while working
    on your assignment
  * **However**, you will need to remove your own testing code, and
    re-run the original testing script right before you submit the
    code, to ensure your code is free from syntax errors
* If you are using the Colab notebook version, after you finished your work, please download this notebook as **python** file
  (not notebook file)
  * on menu bar (Colab's menu bar, NOT your browser's menu bar), go to File -> Download -> Download .py
"""

#===== Import section begins
import collections
import heapq
# In this assignment, ONLY given external libraries are allowed
# DO NOT ADD any import statements
# keep this section as is
#===== Import section ends


#===== Provided Global variables section begins
# These global variable(s) are provided as part of the assignment
# DO NOT ADD any other global variables
# keep this section as is
STOPWORDS = [
    'i','me','my','myself','we','our','ours','ourselves','you','your','yours',
    'yourself','yourselves','he','him','his','himself','she','her','hers',
    'herself','it','its','itself','they','them','their','theirs','themselves',
    'what','which','who','whom','this','that','these','those','am','is','are',
    'was','were','be','been','being','have','has','had','having','do','does',
    'did','doing','a','an','the','and','but','if','or','because','as','until',
    'while','of','at','by','for','with','about','against','between','into',
    'through','during','before','after','above','below','to','from','up','down',
    'in','out','on','off','over','under','again','further','then','once','here',
    'there','when','where','why','how','all','any','both','each','few','more',
    'most','other','some','such','no','nor','not','only','own','same','so',
    'than','too','very','s','t','can','will','just','don','should','now'
]
#===== Provided Global variables section ends


#===== Helper classes/functions section begins
# You may add your own classes or functions within this section
# **class** and **function** only!
# any statement that is not encapsulated inside a class or function
# may result in 0 grade

#===== Helper classes/functions section ends


#===== Problem B function begins
# follow the instruction below
# DO NOT change the function signature!
def getTopWords(words: 'List[str]', K: int) -> 'List[str]':
    '''
    - Parameters:
        - words: a list of words
        - K: The number of words to return (K most frequent words)
    - Returns:
        - List[str]: list of words sorted by the frequency from highest to lowest
    '''
    #===== Your implementation begins here
    # Create empty list to store the lowercase words
    lower_words = []
    for word in words:
        # Convert each word to lowercase
        lower_words.append(word.lower())
    
    # Create empty dictionary to store the counts of each word
    word_counts = {}
    
    # Iterate over each word in the list of lowercase words and check
    for word in lower_words:
        if word not in STOPWORDS:
            # If the word is not a stopword, increment its count in the dictionary
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    
    # Use the collections module to create a Counter object from the dictionary of word counts
    word_counter = collections.Counter(word_counts)
    
    # Sort words by frequency (highest to lowest), then alphabetically
    sorted_words = sorted(word_counter.keys(), key=lambda x: (-word_counter[x], x))
    
    # Return top K words
    return sorted_words[:K]
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

    input_1 = [
        'Cat', 'bat','and', 'a', 'Rat','are', 'singing', 'A', 'bat', 'is',
        'not', 'the', 'black', 'caT', 'An', 'elephant', 'a', 'Rat', 'and', 'a',
        'cat', 'are', 'walking', 'Bat', 'is', 'black', 'but', 'the', 'cat',
        'is', 'white', 'And', 'dog', 'is' 'brown'
    ]
    k_1 = 2
    res_1 = ['cat','bat']


    input_2 = [
        'The','weather','is','sunny','in','SC','The','weather','is','cloudy',
        'the','weather'
    ]
    k_2 = 2
    res_2 = ['weather','cloudy']

    print('Test case 1')
    out_res = getTopWords(input_1, k_1)
    print('Input words:     ', input_1)
    print('Input K:         ', k_1)
    print('Expected result: ', res_1)
    print('Your result:     ', out_res)
    type_match = type(res_1) == type(out_res)
    type_match_str = '==' if type_match else '!='
    print('Return Type:     ', 'type(Expected result)', type_match_str, 'type(Your result)')
    print()

    print('Test case 2')
    out_res = getTopWords(input_2, k_2)
    print('Input words:     ', input_2)
    print('Input K:         ', k_2)
    print('Expected result: ', res_2)
    print('Your result:     ', out_res)
    type_match = type(res_2) == type(out_res)
    type_match_str = '==' if type_match else '!='
    print('Return Type:     ', 'type(Expected result)', type_match_str, 'type(Your result)')
    print()

if __name__ == '__main__':
    main()

#===== Testing scripts main function section ends