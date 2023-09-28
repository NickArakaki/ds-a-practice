"""
Given an m x n grid of characters board and a string word,
return true if word exists in the grid.

The word can be constructed from letters of sequentially
adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.
"""

def exist(board: list[list[str]], word: str) -> bool:
    def _get_neighbors(point):
        row, col = point
        neighbors = []
        # above
        if row - 1 >= 0:
            neighbors.append((row - 1, col))
        # below
        if row + 1 < len(board):
            neighbors.append((row + 1, col))
        # left
        if col - 1 >= 0:
            neighbors.append((row, col - 1))
        # right
        if col + 1 < len(board[0]):
            neighbors.append((row, col + 1))

        return neighbors


    # backtrack algo
        # base cases:
            # if current char != word[i] return False
            # if current char == word[i] && i == len(word) - 1 return True
            #
        # get valid neighbors of current node
    def _backtrack(node, visited, idx):
        r, c = node
        if idx == len(word) - 1 and board[r][c] == word[idx]:
            return True
        if board[r][c] != word[idx]:
            return

        neighbors = _get_neighbors(node)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                if _backtrack(neighbor, visited, idx + 1):
                    return True
                else:
                    visited.remove(neighbor)


    # iterate through board
        # if char == first char in word run back track algo to see if there is any path that forms the word
    for row in range(len(board)):
        for col in range(len(board[0])):
            seen_nodes = set()
            seen_nodes.add((row, col))
            if _backtrack((row, col), seen_nodes, 0):
                return True

    return False

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")) # true
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")) # true
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")) # false
print(exist([["a"]], "a")) # true
