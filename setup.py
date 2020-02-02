from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        'neat.graphs',
        ['neat/graphs.pyx']
    ),
    Extension(
        'neat.nn.feed_forward',
        ['neat/nn/feed_forward.pyx']
    ),
    Extension(
        'neat.activations',
        ['neat/nn/activations.pyx']
    )
]

setup(
    name='neat-python',
    version='0.92',
    author='cesar.gomes, mirrorballu2',
    author_email='nobody@nowhere.com',
    maintainer='CodeReclaimers, LLC',
    maintainer_email='alan@codereclaimers.com',
    url='https://github.com/CodeReclaimers/neat-python',
    license="BSD",
    description='A NEAT (NeuroEvolution of Augmenting Topologies) implementation',
    long_description='Python implementation of NEAT (NeuroEvolution of Augmenting Topologies), a method ' +
                     'developed by Kenneth O. Stanley for evolving arbitrary neural networks.',
    packages=['neat', 'neat/iznn', 'neat/nn', 'neat/ctrnn'],
    ext_modules=cythonize(extensions),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Scientific/Engineering'
    ]
)
