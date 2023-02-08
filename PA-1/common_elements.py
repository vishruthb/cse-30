def common_elements(list_1: list, list_2: list) -> list:
    """
    This function takes two lists as input, and it then returns a list of common 
    elements of the input lists. I found many ways to go about solving this 
    problem, from using the "in" method and a for loop to using nested loops. 
    Despite this, I ended up solving this problem using the set intersection() 
    method, which I believe is more efficient.
    """
    # Converts both input lists into sets.
    list_1 = set(list_1)
    list_2 = set(list_2)
    # Uses intersection() method to identify common elements between the input
    # lists.
    common = list_1.intersection(list_2)
    # Uses list() method to return a numerically sorted list, which is
    # more efficient.
    return list(common)
"""
If the size of one of the input lists is way smaller than the other list, we 
could potentially solve the problem more efficiently by first converting the 
smaller list to a set. Then, like the previous solution, we could use the 
intersection() method to find the common elements between the 
smaller and larger list. 
Here is a potentially more efficient solution:
def common_elements(list_1: list, list_2: list) -> list:
    if len(list_1) > len(list_2):
        smaller = set(list_2)
        common = smaller.intersection(list_1)
    else:
        smaller = set(list_1)
        common = smaller.intersection(list_2)
    return list(common)
"""
