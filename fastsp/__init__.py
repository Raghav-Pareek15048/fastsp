"""
fastsp: High-performance Traveling Salesperson Problem (TSP) solver.
Includes both a pure Python solver and a blazing-fast native C++ solver wrapped with Cython.
"""

__version__ = "0.1.0"

# Import pure Python solver
from .python_solver import tsp_python

# Import Cython wrapper (available once extension is compiled)
try:
    from .tsp_wrapper import tsp_cython
except ImportError:
    try:
        from tsp_wrapper import tsp_cython
    except ImportError:
        tsp_cython = None

__all__ = ["tsp_python", "tsp_cython", "__version__"]

