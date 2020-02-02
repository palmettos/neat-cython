This is a fork of [neat-python](https://github.com/CodeReclaimers/neat-python) (which was created by [CodeReclaimers](https://github.com/CodeReclaimers)). I am not a contributor to the original project. This repository differs from the original project only in that it contains compilable [Cython](https://cython.org/) optimizations in performance-critical modules.

All existing APIs and documentation are functionally equivalent.

## Building ##

To build the Cython extensions, first follow the instructions on [installing Cython](https://cython.readthedocs.io/en/latest/src/quickstart/install.html).

Then, run `python setup.py build_ext --inplace` from the root directory.