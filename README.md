# tsp-fast-solver: High-Performance TSP Solver in Pure Python & C++ (Cython)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A high-performance library solving the **Traveling Salesperson Problem (TSP)** using brute-force search implemented in both **Pure Python** and **Native C++ wrapped with Cython**.

---

## 📌 Problem Overview & Real-World Context

The **Traveling Salesperson Problem (TSP)** is an NP-hard problem in combinatorial optimization:
> Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?

Because the number of unique tours starting from a fixed origin scales factorially with $(N-1)!$, brute-force exploration in dynamic languages like pure Python rapidly encounters performance bottlenecks. 

By offloading the inner combinatorial search loop (`std::next_permutation`) to compiled C++ and exposing it via a zero-overhead Cython C-extension, we achieve up to **~100x speedups**.

---

## 🚀 Performance Benchmarks

Benchmarks were performed on random symmetric Euclidean/metric distance matrices using Python's `timeit` module.

| Graph Size (Nodes) | Possible Routes $(N-1)!$ | Pure Python Time (s) | Cython C++ Time (s) | Speedup | Minimum Tour Cost |
|:------------------:|:------------------------:|:--------------------:|:-------------------:|:-------:|:-----------------:|
| **N = 8**          | 5,040                    | 0.0034s              | **0.00005s**        | **71.5x** | 229               |
| **N = 10**         | 362,880                  | 0.3384s              | **0.0033s**         | **101.7x** | 191               |
| **N = 11**         | 3,628,800                | 3.8315s              | **0.0418s**         | **91.6x**  | 268               |

### Key Takeaways
- **N = 8**: Cython execution is virtually instantaneous ($< 0.1\text{ ms}$).
- **N = 10**: Over $362,000$ permutations evaluated in only $3.3\text{ ms}$ (vs. $338\text{ ms}$ in Python).
- **N = 11**: Evaluates over $3.6\text{ million}$ complete candidate tours in just $41.8\text{ ms}$ (under $0.05$ seconds), delivering a massive **~92x to 102x speedup** over pure Python.

---

## 📂 Project Architecture

```
CPython/
├── pyproject.toml              # Modern PEP 517/518 build specification
├── setup.py                    # Setuptools build configuration with Cython C++ extension
├── MANIFEST.in                 # Source distribution manifest ensuring all C++ & Cython files are packaged
├── .gitignore                  # Git ignore rules for build artifacts, compiled .pyd/.so, etc.
├── README.md                   # Complete documentation and benchmark analysis
├── WORKFLOW_STEPS.txt          # Detailed step-by-step workflow of work performed
├── benchmark.py                # Benchmarking suite comparing Pure Python vs Cython
├── test_solvers.py             # Unit tests verifying correctness and equivalence across topologies
├── src/
│   ├── python_solver/
│   │   ├── __init__.py
│   │   └── solver.py           # Pure Python implementation (tsp_python) using itertools.permutations
│   ├── cpp/
│   │   ├── tsp.h               # C++ header declaring tsp_solver(const std::vector<int>&, int)
│   │   └── tsp.cpp             # Native C++ solver using std::next_permutation
│   └── cython_wrapper/
│       ├── __init__.py
│       ├── tsp_c.pxd           # Cython declaration bridging C++ header
│       └── tsp_wrapper.pyx     # Cython implementation converting list-of-lists to std::vector<int>
└── tsp_fast_solver/            # Python package entry point
    ├── __init__.py             # Exports tsp_python and tsp_cython
    └── python_solver.py        # Packaged pure Python fallback
```

---

## 🛠️ Installation & Building

### 1. Requirements
- Python 3.8 or higher
- C++11 compliant compiler (GCC/MinGW-w64 on Windows, GCC/Clang on Linux/macOS, or MSVC)
- Cython, setuptools, and build:
  ```bash
  pip install cython setuptools build twine pytest
  ```

### 2. In-place Compilation (Local Development)
To compile the C++ extension locally:
```bash
python setup.py build_ext --inplace
```

### 3. Build Source Distribution (sdist)
To generate the distribution tarball for PyPI:
```bash
python -m build --sdist
```
The resulting `.tar.gz` archive will be located in the `dist/` directory.

---

## 💻 Usage Example

```python
from tsp_fast_solver import tsp_python, tsp_cython

# Define an N x N distance matrix (e.g. 4 cities)
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# 1. Pure Python Solver
py_cost = tsp_python(distance_matrix)
print("Pure Python Minimum Cost:", py_cost)

# 2. Cython C++ Solver
cy_cost = tsp_cython(distance_matrix)
print("Cython C++ Minimum Cost:", cy_cost)

assert py_cost == cy_cost
```

---

## 🧪 Running Tests & Benchmarks

### Run Unit Tests
```bash
pytest test_solvers.py -v
```

### Run Benchmarks
```bash
python benchmark.py
```

---

## 📦 Publishing to GitHub and PyPI

### Step 1: Initialize Git and Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit: Pure Python and Cython C++ TSP solvers"
git branch -M main
git remote add origin https://github.com/<your-username>/tsp-fast-solver.git
git push -u origin main
```

### Step 2: Upload to PyPI using Twine
```bash
# Upload distribution archive to PyPI
python -m twine upload dist/*
```
When prompted:
- **Username**: `__token__`
- **Password**: `<Your-PyPI-API-Token>`

### Step 3: Verify Installation from PyPI
```bash
pip install tsp-fast-solver
python -c "import tsp_fast_solver; print('Successfully installed and imported!')"
```

---

## 📄 License
This project is licensed under the MIT License.
