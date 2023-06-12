"""
Given the root of a binary tree, return the level order
traversal of its nodes' values. (i.e., from left to right, level by level).
"""
from collections import deque

def levelOrder(root):
    queue = deque()
    queue.append(root)
    res = []

    while len(queue):
        level = []
        for _ in range(len(queue)):
            curr_node = queue.popleft()
            if curr_node:
                level.append(curr_node.val)
                queue.append(curr_node.left)
                queue.append(curr_node.right)

        if len(level): res.append(level)

    return res
