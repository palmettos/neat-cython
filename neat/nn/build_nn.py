from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        'neat.nn.feed_forward',
        ['neat/nn/feed_forward.pyx']
    )
]

setup(
    name='nn',
    packages=find_packages(),
    ext_modules=cythonize(extensions)
)