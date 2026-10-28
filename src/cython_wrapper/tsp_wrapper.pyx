# distutils: language = c++
# cython: language_level=3

from libcpp.vector cimport vector
from tsp_c cimport tsp_solver

def tsp_cython(distance_matrix):
    """
    Calculates the shortest tour path cost through a fully connected graph
    represented by a 2D distance matrix using the native compiled C++ solver.

    Parameters:
        distance_matrix: Python list-of-lists representing the 2D distance matrix.

    Returns:
        int: The minimum total tour cost visiting each node once and returning to origin node 0.
    """
    cdef int n = len(distance_matrix)
    if n <= 1:
        return 0
    if n == 2:
        return int(distance_matrix[0][1] + distance_matrix[1][0])

    cdef vector[int] vec_1d
    vec_1d.reserve(n * n)

    cdef int i, j
    for i in range(n):
        row = distance_matrix[i]
        for j in range(n):
            vec_1d.push_back(<int>row[j])

    cdef int min_cost = tsp_solver(vec_1d, n)
    return min_cost
