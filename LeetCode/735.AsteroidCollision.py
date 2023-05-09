"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents
its direction (positive meaning right, negative meaning left). Each asteroid moves
at the same speed.

Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.

Constraints:
    2 <= asteroids.length <= 104
    -1000 <= asteroids[i] <= 1000
    asteroids[i] != 0
"""

def asteroidCollision(asteriods):
    # initialize a stack
    stack = []
    # iterate through the asteroids list starting from the second element
    for asteroid in asteriods:
        resolved = False

        while not resolved:
            print(stack)
            print(asteroid)
            # if there is nothing in the stack, or if previous asteroids are moving in same direction
            if not len(stack) or (asteroid > 0 and stack[-1] > 0) or (asteroid < 0 and stack[-1] < 0) or (asteroid > 0 and stack[-1] < 0):
                stack.append(asteroid)
                resolved = True
            elif abs(asteroid) == abs(stack[-1]): # if current asteroid and previous asteroid are same magnitude
                stack.pop()
                resolved = True
            elif abs(asteroid) > abs(stack[-1]): # if current asteroid abs val is greater than previous asteroid
                stack.pop()
                continue
            else: # if the previous asteroid is moving in the opposite direction and the abs val is > current asteroid
                resolved = True
    # return the asteroid stack
    return stack

# print(asteroidCollision([5,10,-5])) # [5, 10]
# print(asteroidCollision([8,-8])) # []
# print(asteroidCollision([10,2,-5])) # [10]
# print(asteroidCollision([3, 2,-5])) # [-5]
print(asteroidCollision([-2,-1,1,2])) # [-2,-1,1,2]
