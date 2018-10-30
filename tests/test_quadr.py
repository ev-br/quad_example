

from __future__ import division, absolute_import, print_function

from numpy.testing import assert_allclose

from ..quadr import quad_solve


def test_two_real_roots():
    assert_allclose(quad_solve(0, -1), (1, -1))


def test_two_cmplx_conj_roots():
    assert_allclose(quad_solve(0, 1), (1j, -1j))


