"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i]
and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.


"""
from collections import deque

def is_valid_binary_tree(root, leftChild, rightChild):
    queue = deque()
    queue.append(root)
    visited = set()
    visited.add(root)

    while queue:
        cur_node = queue.popleft()
        l_child = leftChild[cur_node]
        r_child = rightChild[cur_node]

        if l_child != -1:
            if l_child in visited:
                return False
            visited.add(l_child)
            queue.append(l_child)

        if r_child != -1:
            if r_child in visited:
                return False
            visited.add(r_child)
            queue.append(r_child)

    return True if len(visited) == len(leftChild) else False


def validate_binary_tree_nodes(n: int, leftChild: list[int], rightChild: list[int]) -> bool:
    # create list child_count of len n, tracks which nodes have parents
    has_parent_list = [False] * n
    for node in range(n):
        l_child = leftChild[node]
        r_child = rightChild[node]

        if l_child > -1: has_parent_list[l_child] = True
        if r_child > -1: has_parent_list[r_child] = True

    # init root tracker -1
    cur_root = -1
    for node, has_parent in enumerate(has_parent_list):
        if not has_parent:
            if cur_root == -1:
                cur_root = node
            else:
                return False

    return is_valid_binary_tree(cur_root, leftChild, rightChild)


# def is_valid_bin_tree(root: int, left_children: list[int], right_children: list[int]) -> bool:
#         queue = deque()
#         queue.append(root)

#         visited = set()
#         visited.add(root)

#         while queue:
#             cur_node = queue.popleft()
#             l_child = left_children[cur_node]
#             r_child = right_children[cur_node]

#             if l_child != -1:
#                 if l_child in visited:
#                     return False
#                 queue.append(l_child)
#                 visited.add(l_child)

#             if r_child != -1:
#                 if r_child in visited:
#                     return False
#                 queue.append(r_child)
#                 visited.add(r_child)

#         return True if len(visited) == len(left_children) else False


# def validate_binary_tree_nodes(n: int, leftChild: list[int], rightChild: list[int]) -> bool:
#     # track which nodes have parents
#     has_parent_list = [False] * n
#     for node in range(n):
#         l_node = leftChild[node]
#         r_node = rightChild[node]

#         if l_node > -1:
#             has_parent_list[l_node] = True
#         if r_node > -1:
#             has_parent_list[r_node] = True

#     root = -1
#     for node, has_parent in enumerate(has_parent_list):
#         if not has_parent:
#             if root == -1:
#                 root = node
#             else:
#                 return False

#     return is_valid_bin_tree(root, leftChild, rightChild)

print(validate_binary_tree_nodes(4, [1,-1,3,-1], [2,-1,-1,-1]) == True)
print(validate_binary_tree_nodes(4, [1,-1,3,-1], [2,3,-1,-1]) == False)
print(validate_binary_tree_nodes(2, [1,0], [-1, -1]) == False)
print(validate_binary_tree_nodes(4, [3,-1,1,-1], [-1,-1,0,-1]) == True)
