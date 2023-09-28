"""
Design a system that manages the reservation state of n seats that are numbered from 1 to n.

Implement the SeatManager class:

SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.
"""

import heapq

class SeatManager:

    def __init__(self, n: int):
        self.seats = [i + 1 for i in range(n)]
        heapq.heapify(self.seats)


    def reserve(self) -> int:
        return heapq.heappop(self.seats)


    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)


seatTest = SeatManager(5)
print(seatTest.seats) # [1,2,3,4,5]

seatTest.reserve()
print(seatTest.seats) # [2,3,4,5]

seatTest.reserve()
print(seatTest.seats) # [3,4,5]

seatTest.unreserve(2)
print(seatTest.seats) # [2,3,4,5]

seatTest.reserve()
print(seatTest.seats) # [3,4,5]

seatTest.reserve()
print(seatTest.seats) # [4,5]

seatTest.reserve()
print(seatTest.seats) # [5]

seatTest.reserve()
print(seatTest.seats) # []

seatTest.unreserve(5)
print(seatTest.seats) # [5]
