"""
There is an infrastructure of n cities with some number of roads connecting these cities.
Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected
roads to either city. If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.
"""

from collections import defaultdict
from itertools import combinations


def maximal_network_rank(n: int, roads: list[list[int]]) -> int:
    graph = defaultdict(set)

    for city_1, city_2 in roads:
        graph[city_1].add(city_2)
        graph[city_2].add(city_1)

    cities = graph.keys()
    rank = 0
    for city1 in cities:
        for city2 in cities:
            if city1 == city2:
                continue
            # for city_1, city_2 in combinations(graph.keys(), 2):
            has_connection = 1 if city1 in graph[city2] else 0
            city1_connections = len(graph[city1])
            city2_connections = len(graph[city2])

            rank = max(rank, city1_connections +
                       city2_connections - has_connection)

    return rank


print(maximal_network_rank(4, [[0, 1], [0, 3], [1, 2], [1, 3]]) == 4)
print(maximal_network_rank(
    5, [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]) == 5)
