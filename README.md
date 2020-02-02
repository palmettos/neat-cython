[![Build Status](https://travis-ci.org/CodeReclaimers/neat-python.svg)](https://travis-ci.org/CodeReclaimers/neat-python)
[![Coverage Status](https://coveralls.io/repos/CodeReclaimers/neat-python/badge.svg?branch=master&service=github)](https://coveralls.io/github/CodeReclaimers/neat-python?branch=master)

This is a fork of [neat-python](https://github.com/CodeReclaimers/neat-python) which was created by [CodeReclaimers](https://github.com/CodeReclaimers). I am not a contributor to the original project. This repository differs from the original project only in that it contains compilable [Cython](https://cython.org/) optimizations in performance-critical modules.

## About ##

NEAT (NeuroEvolution of Augmenting Topologies) is a method developed by Kenneth O. Stanley for evolving arbitrary neural
networks. This project is a pure-Python implementation of NEAT with no dependencies beyond the standard library. It was
forked from the excellent project by @MattKallada, and is in the process of being updated to provide more features and a
(hopefully) simpler and documented API.

For further information regarding general concepts and theory, please see
[Selected Publications](http://www.cs.ucf.edu/~kstanley/#publications) on Stanley's website.

`neat-python` is licensed under the [3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).

## Building ##

To build the Cython extensions, first follow the instructions on [installing Cython](https://cython.readthedocs.io/en/latest/src/quickstart/install.html).

Then, run `python setup.py build_ext --inplace` from the root directory.

## Getting Started ##

If you want to try neat-python, please check out the repository, start playing with the examples (`examples/xor` is
a good place to start) and then try creating your own experiment.

The documentation, is available on [Read The Docs](http://neat-python.readthedocs.io).

## Citing ##

Here is a Bibtex entry you can use to cite this project in a publication. The listed authors are the maintainers of
all iterations of the project up to this point. 

```
@misc{neat-python,
    Title = {neat-python},
    Author = {Alan McIntyre and Matt Kallada and Cesar G. Miguel and Carolina Feher da Silva},
    howpublished = {\url{https://github.com/CodeReclaimers/neat-python}}   
  }
```