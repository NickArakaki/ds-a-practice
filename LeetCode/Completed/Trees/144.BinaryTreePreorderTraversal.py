"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""

def preorderTraversal(root):
    if root is None: return []
    left = preorderTraversal(root.left)
    right = preorderTraversal(root.right)
    return [root.val] + left + right
