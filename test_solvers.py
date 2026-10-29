"""
Unit tests for TSP Solvers (Pure Python and Cython C++ wrapper).
"""

import pytest
try:
    from fastsp import tsp_python, tsp_cython
except ImportError:
    from tsp_fast_solver import tsp_python, tsp_cython


def test_edge_cases():
    # Empty graph
    assert tsp_python([]) == 0
    assert tsp_cython([]) == 0

    # 1 node
    assert tsp_python([[0]]) == 0
    assert tsp_cython([[0]]) == 0

    # 2 nodes
    dist_2 = [
        [0, 15],
        [20, 0]
    ]
    assert tsp_python(dist_2) == 35
    assert tsp_cython(dist_2) == 35


def test_known_triangle_graph():
    dist_3 = [
        [0, 10, 20],
        [10, 0, 15],
        [20, 15, 0]
    ]
    # Possible routes from 0:
    # 0 -> 1 -> 2 -> 0 = 10 + 15 + 20 = 45
    # 0 -> 2 -> 1 -> 0 = 20 + 15 + 10 = 45
    assert tsp_python(dist_3) == 45
    assert tsp_cython(dist_3) == 45


def test_4_node_graph():
    dist_4 = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    # Optimal: 0 -> 1 -> 3 -> 2 -> 0: 10 + 25 + 30 + 15 = 80
    assert tsp_python(dist_4) == 80
    assert tsp_cython(dist_4) == 80


def test_equivalence_random_graphs():
    import random
    rng = random.Random(12345)

    for n in [4, 5, 6, 7]:
        matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                val = rng.randint(1, 100)
                matrix[i][j] = val
                matrix[j][i] = val

        py_res = tsp_python(matrix)
        cy_res = tsp_cython(matrix)
        assert py_res == cy_res, f"Failed at N={n}: Python {py_res} != Cython {cy_res}"


if __name__ == "__main__":
    test_edge_cases()
    test_known_triangle_graph()
    test_4_node_graph()
    test_equivalence_random_graphs()
    print("All unit tests passed successfully!")
