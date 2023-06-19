"""
Given the root of a binary tree, invert the tree,
and return its root
"""

def invertTree(root):
    # post order traversal
    # swap left and right nodes
    if root is None: return

    invertTree(root.left)
    invertTree(root.right)
    root.left, root.right = root.right, root.left
    return root
