

from __future__ import division, absolute_import, print_function

from numpy.testing import assert_allclose

from ..quadr import quad_solve


def test_two_real_roots():
    assert_allclose(quad_solve(0, -1), (1, -1))


def test_two_cmplx_conj_roots():
    assert_allclose(quad_solve(0, 1), (1j, -1j))


def test_large_b():
    # Use Viet's theorem
    b, c = 1e20, 1
    x1, x2 = quad_solve(b, c)
    assert_allclose(x1*x2, c)
