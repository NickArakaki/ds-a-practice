"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes
in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def diameter_of_binary_tree(root):
    max_diameter = 0

    def _dft(root):
        nonlocal max_diameter
        if root is None:
            return 0

        depth_left = _dft(root.left)
        depth_right = _dft(root.right)
        curr_diameter = depth_left + depth_right

        if curr_diameter > max_diameter:
            max_diameter = curr_diameter

        return max(depth_left, depth_right) + 1

    _dft(root)
    return max_diameter

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)

print(diameter_of_binary_tree(root))
