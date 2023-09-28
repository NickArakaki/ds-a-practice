"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the
longest path from the root node down to the farthest leaf node.
"""

def max_depth(root) -> int:
    if root is None:
        return 0

    left = max_depth(root.left)
    right = max_depth(root.right)

    return max(left, right) + 1
