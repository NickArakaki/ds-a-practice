"""
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
"""

def safe_states(graph: list[list[int]]) -> list[int]:
    safe = {}

    def _is_safe():
        pass

    res = []
    for node in range(len(graph)):
        if _is_safe(node):
            res.append(node)

    return res


print(safe_states([[1,2],[2,3],[5],[0],[5],[],[]]) == [2,4,5,6])
print(safe_states([[1,2,3,4],[1,2],[3,4],[0,4],[]]) == [4])
