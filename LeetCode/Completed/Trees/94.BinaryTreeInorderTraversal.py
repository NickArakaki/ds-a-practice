"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""

def inorderTraversal(root):
    # dfs
    res = []
    stack = [root]
    curr_node = root

    while len(stack):
        if curr_node.left:
            stack.append(curr_node.left)
            curr_node = curr_node.left
        else:
            curr_node = stack.pop()
            res.append(curr_node.val)
            if curr_node.right:
                stack.append(curr_node.right)
                curr_node = curr_node.right

    return res
