from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        'neat.graphs',
        ['neat/graphs.pyx']
    )
]

setup(
    name='graphs',
    packages=find_packages(),
    ext_modules=cythonize(extensions)
)