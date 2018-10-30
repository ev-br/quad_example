

from __future__ import division, absolute_import, print_function


from cmath import sqrt as c_sqrt
from math import sqrt

def quad_solve(b, c):
    """Find two roots of $x^2 + b*x + c = 0$."""
    d = b**2 - 4*c
    sqd = sqrt(d) if d >= 0 else c_sqrt(d)
    x1, x2 = (-b + sqd) / 2, (-b - sqd) / 2
    return x1, x2

if __name__ == "__main__":
    from numpy.testing import assert_allclose
    assert_allclose(quad_solve(0, -1), (1, -1))
    assert_allclose(quad_solve(0, 1), (1j, -1j))
# TODO: do something for extremely large b
#       assert_allclose(quad_solve(1e20, 1), )
