"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i]
and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.


"""

def validate_binary_tree_nodes(n: int, leftChild: list[int], rightChild: list[int]) -> bool:
    pass


print(validate_binary_tree_nodes(4, [1,-1,3,-1], [2,-1,-1,-1]) == True)
print(validate_binary_tree_nodes(4, [1,-1,3,-1], [2,3,-1,-1]) == False)
print(validate_binary_tree_nodes(n = 2, leftChild = [1,0], rightChild = [-1,-1]) == False)
