"""
Pure Python Traveling Salesperson Problem (TSP) Brute-Force Solver.
Uses itertools.permutations to explore all (N-1)! possible routes.
"""

import itertools
from typing import Sequence, Union

def tsp_python(distance_matrix: Sequence[Sequence[Union[int, float]]]) -> Union[int, float]:
    """
    Calculates the shortest tour path cost through a fully connected graph
    represented by a 2D distance matrix using brute-force search.

    Parameters:
        distance_matrix: 2D square matrix where distance_matrix[i][j] is the distance from node i to j.

    Returns:
        The minimum total tour cost visiting each node once and returning to the origin (node 0).
    """
    n = len(distance_matrix)
    if n <= 1:
        return 0
    if n == 2:
        return distance_matrix[0][1] + distance_matrix[1][0]

    cities = list(range(1, n))
    min_cost = float("inf")

    for perm in itertools.permutations(cities):
        # Start at city 0 -> perm[0]
        cost = distance_matrix[0][perm[0]]
        
        # Traverse intermediate cities in permutation order
        for i in range(len(perm) - 1):
            cost += distance_matrix[perm[i]][perm[i + 1]]
            
        # Return to origin city 0 from the last city
        cost += distance_matrix[perm[-1]][0]

        if cost < min_cost:
            min_cost = cost

    return min_cost
