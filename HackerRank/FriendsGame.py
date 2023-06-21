def friendsGame(friends: int, time: int) -> list[int]:
    time_friend_int_div = time // (friends - 1)
    remainder = time % (friends - 1)

    if (time_friend_int_div % 2 == 1 and remainder == 0) or (time_friend_int_div % 2 == 0 and remainder > 0):
        ending_friend = friends if remainder == 0 else remainder + 1
        previous_friend = ending_friend - 1
    else:
        ending_friend = 1 if remainder == 0 else friends - remainder
        previous_friend = ending_friend + 1

    return [previous_friend, ending_friend]

print(friendsGame(5, 3)) # [3, 4]
print(friendsGame(4, 3)) # [3, 4]
print(friendsGame(4, 6)) # [2, 1]
