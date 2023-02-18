"""
Author: Vishruth Bharath
Class: W2023 CSE 30
Objective: To build a class that class that evaluates an expression represented as a string.
"""

class EvalExpression:

    def evaluate(self, s: str) -> int:
        '''

         - Parameters:

            - s : expression to be evaluated

         - Returns:

            - int : result of the expression



        Iterate through the expression and calculate the expression using stacks.

        '''
        # If inputted expression is empty, return 0
        if not s: return 0

        # Remove spaces in expression and initialize variables to store results
        s = s.replace(" ", "")
        num, prev, res = 0, 0, 0
        op = "+"
        # Iterate through the input expression, get number and operator, and complete task
        i = 0
        while i < len(s):
            char = s[i]
            if char.isdigit():
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                i -= 1
                if op == "+":
                    res += num
                    prev = num
                elif op == "-":
                    res -= num
                    prev = -num
                elif op == "*":
                    res -= prev
                    res += prev * num
                    prev = prev * num
                elif op == "/":
                    res -= prev
                    res += int(prev / num)
                    prev = int(prev / num)
                # Reset
                num = 0
            else:
                # Save current operator
                op = char
            i += 1
        # Return the final result as an integer
        return res
