#!/usr/bin/env python3
from distutils.core import setup
from Cython.Build import cythonize

extensions = ["spacegame.pyx"]

setup(
    name = "Spacegame",
    ext_modules = cythonize(extensions),

)
