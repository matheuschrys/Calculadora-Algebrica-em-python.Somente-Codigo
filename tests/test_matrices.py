from math import isclose

import pytest

from calculadora_algebra.matrices import (
    matrix_vector_multiply,
    normalize_vector,
    power_iteration,
    validate_square_matrix,
)


def test_matrix_vector_multiply():
    matrix = [[1, 2], [3, 4]]
    assert matrix_vector_multiply(matrix, [5, 6]) == [17, 39]


def test_normalize_vector():
    normalized = normalize_vector([3, 4])
    assert normalized == [0.6, 0.8]
    assert normalize_vector([0, 0]) == [0.0, 0.0]


def test_power_iteration_finds_dominant_eigenvalue_for_diagonal_matrix():
    eigenvalue, eigenvector = power_iteration([[2, 0], [0, 3]], max_iter=200, tolerance=1e-10)
    assert isclose(eigenvalue, 3, rel_tol=1e-5)
    assert abs(eigenvector[1]) > abs(eigenvector[0])


def test_validate_square_matrix_rejects_non_square_matrix():
    with pytest.raises(ValueError, match="matriz"):
        validate_square_matrix([[1, 2, 3], [4, 5, 6]])
