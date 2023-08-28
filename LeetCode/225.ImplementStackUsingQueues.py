"""
Implement a last-in-first-out (LIFO) stack using only two queues.
The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back,
peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively.
You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
"""

from collections import deque

class MyStack:
    def __init__(self):
        self.stack = deque()


    def push(self, x: int) -> None:
        """
        pushes element x to top of the stack
        """
        self.stack.append(x)


    def pop(self) -> int:
        """
        Removes the element on the top of the stack
        """
        i = 0
        while i < len(self.stack) - 1:
            el = self.stack.popleft()
            self.stack.append(el)
            i += 1
        return self.stack.popleft()


    def top(self) -> int:
        """
        Returns the top element on the top of the stack
        """
        last_el = None
        for el in self.stack:
            last_el = el
        return last_el



    def empty(self) -> bool:
        """
        Returns True if stack is empty, False otherwise
        """
        return len(self.stack) == 0


# Test Cases
obj = MyStack()
print(obj.push(1))
print(obj.push(2))
print(obj)
print(obj.top())
print(obj.pop())
print(obj.empty())
print(obj.pop())
print(obj.empty())
print(obj.pop())
print(obj.empty())
