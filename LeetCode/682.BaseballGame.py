"""
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.
"""

def calPoints(operations):
# intialize a stack to house the score values
    score_stack = []
    # initialize a variable to track the total sum in the stack
    total = 0
    # iterate through the list
    for operation in operations:
        if operation == "+":
        # if the char is "+" add the previous two from the score stack, push the sum to the top of the score stack
            last_el = score_stack[-1]
            second_last_el = score_stack[-2]
            score_stack.append(last_el + second_last_el)
            total += (last_el + second_last_el)
        elif operation == "D":
        # if the char is "D" get the most recent value added to the score stack, double it and push it to the top of the stack
            last_el = score_stack[-1]
            score_stack.append(last_el * 2)
            total += (last_el * 2)
        elif operation == "C":
        # if the char is "C" remove the previous score added to the score stack
            last_el = score_stack.pop()
            total -= last_el
        else:
        # everything else we can assume is an int and push the value as an integer to the score stack
            score_stack.append(int(operation))
            total += int(operation)

    # return the total sum of the stack
    return total

print(calPoints(["5","2","C","D","+"])) # 30
print(calPoints(["5","-2","4","C","D","9","+","+"])) # 27
print(calPoints(["1","C"])) # 0
