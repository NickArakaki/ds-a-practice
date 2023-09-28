"""
Given the root of a Binary Search Tree (BST),
return the minimum absolute difference between
the values of any two different nodes in the tree.
"""
from collections import deque

def getMinimumDifference(root) -> int:
    # initialize a var to track global min
    # set up a helper dft pre-order processing
    def _dfs_max(node) -> int:
        if node is None: return float("-inf")
        return max(node.val , _dfs_max(node.right))


    def _dfs_min(node) -> int:
        if node is None: return float("inf")
        return min(node.val, _dfs_min(node.left))


    def _find_min_diff(node) -> int:
        min_diff = float("inf")
        queue = deque()
        queue.append(node)

        while queue:
            curr_node = queue.popleft()
            left_val = right_val = float("inf")

            if curr_node.left:
                left_val = _dfs_max(curr_node.left)
                queue.append(curr_node.left)

            if curr_node.right:
                right_val = _dfs_min(curr_node.right)
                queue.append(curr_node.right)

            left_diff = abs(curr_node.val - left_val)
            right_diff = abs(curr_node.val - right_val)
            min_diff = min(min_diff, left_diff, right_diff)

        return min_diff

    return _find_min_diff(root)
