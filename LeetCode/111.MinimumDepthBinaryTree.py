"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the
shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""

from collections import deque

def min_depth(root) -> int:
    if root is None: return 0

    queue = deque()
    queue.append((root, 1))

    while queue:
        curr_node, level = queue.popleft()
        left_node = curr_node.left
        right_node = curr_node.right

        if not left_node and not right_node:
            return level

        if left_node:
            queue.append((left_node, level + 1))
        if right_node:
            queue.append((right_node, level + 1))
