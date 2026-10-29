"""
Benchmarking Pure Python vs. Cython C++ TSP Solvers.
Measures execution time on graph sizes N=8, N=10, and N=11 using the timeit module.
"""

import math
import random
import timeit
from typing import List

try:
    from fastsp import tsp_python, tsp_cython
except ImportError:
    from tsp_fast_solver import tsp_python, tsp_cython


def generate_distance_matrix(n: int, seed: int = 42, max_dist: int = 100) -> List[List[int]]:
    """
    Generates a symmetric 2D distance matrix with zeros on diagonal
    and random integer distances between distinct pairs of nodes.
    """
    rng = random.Random(seed + n)
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = rng.randint(5, max_dist)
            matrix[i][j] = d
            matrix[j][i] = d
    return matrix


def run_benchmark():
    sizes = [8, 10, 11]
    results = []

    print("=" * 80)
    print("Traveling Salesperson Problem (TSP) Brute-Force Solver Benchmark")
    print("=" * 80)
    print(f"{'Graph Size (N)':<15} | {'Possible Routes (N-1)!':<24} | {'Python Time':<15} | {'Cython Time':<15} | {'Speedup':<10}")
    print("-" * 80)

    for n in sizes:
        matrix = generate_distance_matrix(n)
        routes = math.factorial(n - 1)

        # Benchmark Python implementation
        t0 = timeit.default_timer()
        py_cost = tsp_python(matrix)
        t_python = timeit.default_timer() - t0

        # Benchmark Cython C++ implementation
        t0 = timeit.default_timer()
        cy_cost = tsp_cython(matrix)
        t_cython = timeit.default_timer() - t0

        # Verify correctness
        assert py_cost == cy_cost, f"Mismatch at N={n}: Python={py_cost}, Cython={cy_cost}"

        speedup = t_python / t_cython if t_cython > 0 else float("inf")

        results.append({
            "n": n,
            "routes": routes,
            "py_time": t_python,
            "cy_time": t_cython,
            "speedup": speedup,
            "min_cost": py_cost
        })

        print(f"N = {n:<11} | {routes:<24,d} | {t_python:<13.5f}s | {t_cython:<13.5f}s | {speedup:<8.1f}x")

    print("=" * 80)
    print("\nBenchmark Summary (Markdown format for README.md):")
    print("| Graph Size (Nodes) | Possible Routes (N-1)! | Python Time (s) | Cython Time (s) | Speedup | Minimum Tour Cost |")
    print("|:------------------:|:----------------------:|:---------------:|:---------------:|:-------:|:-----------------:|")
    for r in results:
        print(f"| N = {r['n']} | {r['routes']:,} | {r['py_time']:.4f}s | {r['cy_time']:.4f}s | **{r['speedup']:.1f}x** | {r['min_cost']} |")

    return results


if __name__ == "__main__":
    run_benchmark()
