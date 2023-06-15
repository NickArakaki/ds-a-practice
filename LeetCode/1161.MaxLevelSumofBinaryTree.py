"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

leaf_node_one = TreeNode(7)
leaf_node_two = TreeNode(-8)
edge_node_one = TreeNode(7, leaf_node_one, leaf_node_two)
edge_node_two = TreeNode(0)
root_node = TreeNode(1, edge_node_one, edge_node_two)

def maxLevelSum(root) -> int:
        # two vars to track global max and what level
        max_sum = float("-inf")
        min_level = level = 1
        queue = deque()
        queue.append([root])
        # bft to get sum of each level, if current sum > global max update global vars
        while level < len(queue):
            curr_level = queue.popleft()
            curr_sum = 0
            children = []

            for node in curr_level:
                curr_sum += node.val
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)

            if len(children):
                queue.append(children)

            if curr_sum > max_sum:
                max_sum = curr_sum
                min_level = level

            level += 1

        # return level
        return level

print(maxLevelSum(root_node)) # 2
