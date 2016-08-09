# -*- coding: utf-8 -*-
import pytest

FIBONACCI_TABLE = [
    (-5, -1),
    (0, -1),
    ('string', -2),
    (1, 0),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 3),
    (6, 5),
    (7, 8),
    (8, 13),
]

LUCAS_TABLE = [
    (-5, -1),
    (0, -1),
    ('string', -2),
    (1, 2),
    (2, 1),
    (3, 3),
    (4, 4),
    (5, 7),
    (6, 11),
    (7, 18),
    (8, 29),
]


@pytest.mark.parametrize('n, result', FIBONACCI_TABLE)
def test_fibonacci_iter(n, result):
    from series import fibonacci_iter
    assert fibonacci_iter(n) == result


@pytest.mark.parametrize('n, result', FIBONACCI_TABLE)
def test_fibonacci_rec(n, result):
    from series import fibonacci_rec
    assert fibonacci_rec(n) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas(n, result):
    from series import lucas
    assert lucas(n) == result