"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i]
and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.


"""

def validate_binary_tree_nodes(n: int, leftChild: list[int], rightChild: list[int]) -> bool:
    # create a set of nodes, init with 0th node
    node_set = set()
    node_set.add(0)
    for parent in range(n):
        l_child = leftChild[parent]
        r_child = rightChild[parent]
        if (parent not in node_set) or (l_child in node_set) or (r_child in node_set):
            return False
        if l_child > 0: node_set.add(l_child)
        if r_child > 0: node_set.add(r_child)
    return True

print(validate_binary_tree_nodes(4, [1,-1,3,-1], [2,-1,-1,-1]) == True)
print(validate_binary_tree_nodes(4, [1,-1,3,-1], [2,3,-1,-1]) == False)
print(validate_binary_tree_nodes(n = 2, leftChild = [1,0], rightChild = [-1,-1]) == False)
