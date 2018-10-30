

from __future__ import division, absolute_import, print_function


from math import sqrt

def quad_solve(b, c):
    """Find two roots of $x^2 + b*x + c = 0$."""
    d = b**2 - 4*c
    x1, x2 = (-b + sqrt(d)) / 2, (-b - sqrt(d)) / 2
    return x1, x2

if __name__ == "__main__":
    from numpy.testing import assert_allclose
    assert_allclose(quad_solve(0, -1), (1, -1))


