from math import isclose

import pytest

from calculadora_algebra.vectors import add_vectors, distance, dot_product, norm, subtract_vectors


def test_add_vectors_accepts_multiple_vectors():
    assert add_vectors([1, 2, 3], [4, 5, 6], [0.5, 0.5, 0.5]) == [5.5, 7.5, 9.5]


def test_subtract_vectors_from_first_vector():
    assert subtract_vectors([10, 8, 6], [1, 2, 3], [4, 1, 0]) == [5.0, 5.0, 3.0]


def test_dot_product_norm_and_distance():
    assert dot_product([1, 2, 3], [4, 5, 6]) == 32
    assert isclose(norm([3, 4]), 5)
    assert isclose(distance([1, 2], [4, 6]), 5)


def test_operations_reject_different_dimensions():
    with pytest.raises(ValueError, match="dimensao"):
        add_vectors([1, 2], [1])
