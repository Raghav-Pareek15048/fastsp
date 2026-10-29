import os
import sys
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

# Locate C++ and Cython source directories
# Relative /-separated paths for portability and pip build compatibility
CPP_DIR = "src/cpp"
CYTHON_DIR = "src/cython_wrapper"

cpp_source = "src/cpp/tsp.cpp"
pyx_source = "src/cython_wrapper/tsp_wrapper.pyx"

# Common extension configuration
ext_modules = [
    Extension(
        name="fastsp.tsp_wrapper",
        sources=[pyx_source, cpp_source],
        include_dirs=[CPP_DIR, CYTHON_DIR],
        language="c++",
        extra_compile_args=["-O3", "-std=c++11"],
        extra_link_args=["-static", "-static-libgcc", "-static-libstdc++"],
    ),
]

setup(
    name="fastsp",
    version="0.1.0",
    description="A blazing fast C++ TSP solver wrapped in Cython",
    packages=find_packages(),
    ext_modules=cythonize(
        ext_modules,
        include_path=[CYTHON_DIR, CPP_DIR],
        language_level="3",
    ),
)
