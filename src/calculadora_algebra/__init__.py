"""Funcoes reutilizaveis para uma calculadora de algebra linear."""

from .matrices import matrix_vector_multiply, normalize_vector, power_iteration
from .vectors import (
    add_vectors,
    distance,
    dot_product,
    norm,
    subtract_vectors,
    validate_same_dimension,
)

__all__ = [
    "add_vectors",
    "distance",
    "dot_product",
    "matrix_vector_multiply",
    "norm",
    "normalize_vector",
    "power_iteration",
    "subtract_vectors",
    "validate_same_dimension",
]
