"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return
the subtree rooted with that node. If such a node does not exist, return null.
"""

def searchBST(root, val):
    if not root: return None

    if val == root.val: return root
    elif val < root.val: return searchBST(root.left, val)
    else: return searchBST(root.right, val)
