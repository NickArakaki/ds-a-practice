"""
There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'.
You are given a string colors of length n where colors[i] is the color of the ith piece.

Alice and Bob are playing a game where they take alternating turns removing pieces from the line.
In this game, Alice moves first.

Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'.
She is not allowed to remove pieces that are colored 'B'.
Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'.
He is not allowed to remove pieces that are colored 'A'.
Alice and Bob cannot remove pieces from the edge of the line.
If a player cannot make a move on their turn, that player loses and the other player wins.
Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.
"""

def winner_of_game(colors: str) -> bool:
    # track num alice moves
    # track num bob moves
    # iterate thru str with sliding window of len 3
        # if prev char == cur char == next char:
            # increment appripriate counter
    # return alice moves > bob moves
    pass


print(winner_of_game("AAABABB") == True)
"""
    Alice moves first and removes the second "A" because it is the only "A" whose neighbors are both "A"
    Bob moves next and cannot take his turn since there are no "B"s whose neighbors are both "B"
    Alice wins, return True
"""

print(winner_of_game("AA") == False)
"""
    Alice moves first and there are only 2 "A"s and both are on the edge of the line, so she cannot move on her turn
    Bob wins, return False
"""

print(winner_of_game("ABBBBBBBAAA") == False)
"""
    Alice moves first, her only option is to remove the second to last "A"
    Bob moves next, and he can pick many options.
    Alice moves next, she has no moves
    Bob wins, return True
"""
