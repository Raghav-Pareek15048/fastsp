# distutils: language = c++
from libcpp.vector cimport vector

cdef extern from "tsp.h":
    int tsp_solver(const vector[int]& dist_matrix, int n)
