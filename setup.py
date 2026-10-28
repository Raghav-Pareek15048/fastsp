import os
import sys
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

# Locate C++ and Cython source directories
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CPP_DIR = os.path.join(BASE_DIR, "src", "cpp")
CYTHON_DIR = os.path.join(BASE_DIR, "src", "cython_wrapper")

cpp_source = os.path.join(CPP_DIR, "tsp.cpp")
pyx_source = os.path.join(CYTHON_DIR, "tsp_wrapper.pyx")

# Common extension configuration
ext_modules = [
    Extension(
        name="tsp_fast_solver.tsp_wrapper",
        sources=[pyx_source, cpp_source],
        include_dirs=[CPP_DIR, CYTHON_DIR],
        language="c++",
        extra_compile_args=["-O3", "-std=c++11"],
        extra_link_args=["-static", "-static-libgcc", "-static-libstdc++"],
    ),
]

setup(
    name="tsp-fast-solver",
    version="0.1.0",
    description="A blazing fast C++ TSP solver wrapped in Cython",
    packages=find_packages(),
    ext_modules=cythonize(
        ext_modules,
        include_path=[CYTHON_DIR, CPP_DIR],
        language_level="3",
    ),
)
