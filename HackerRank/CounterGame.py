from math import floor, log2

def counterGame(n):
    turn = 0
    while n > 1:
        if log2(n) != floor(log2(n)):
            n -= 2 ** (floor(log2(n)))
        else:
            n //= 2
        if n == 1: break
        turn += 1

    return "Louise" if turn % 2 == 0 else "Richard"

print(counterGame(6)) # Richard
print(counterGame(132)) # Louise
