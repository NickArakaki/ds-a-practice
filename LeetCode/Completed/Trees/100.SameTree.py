"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

"""
from collections import deque

def isSameTree(p, q) -> bool:
    p_queue = deque()
    q_queue = deque()

    p_queue.append(p)
    q_queue.append(q)

    while len(p_queue) and len(q_queue):
        # some logic
        curr_p_node = p_queue.popleft()
        curr_q_node = q_queue.popleft()

        if (curr_p_node and not curr_q_node) or (not curr_p_node and curr_q_node): return False

        if curr_p_node and curr_q_node:
            if curr_p_node.val != curr_q_node.val: return False

            p_queue.append(curr_p_node.left)
            p_queue.append(curr_p_node.right)

            q_queue.append(curr_q_node.left)
            q_queue.append(curr_q_node.right)

    return True
