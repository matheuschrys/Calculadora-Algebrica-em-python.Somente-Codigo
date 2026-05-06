"""Operacoes com matrizes usadas pela calculadora."""

from typing import Sequence

from .vectors import Number, Vector, dot_product, norm

Matrix = list[list[float]]


def validate_square_matrix(matrix: Sequence[Sequence[Number]]) -> None:
    """Valida se a matriz e quadrada e nao vazia."""
    if not matrix:
        raise ValueError("A matriz nao pode ser vazia.")

    size = len(matrix)
    for index, row in enumerate(matrix, start=1):
        if len(row) != size:
            raise ValueError(
                f"A linha {index} tem {len(row)} colunas, "
                f"mas a matriz deveria ter {size}."
            )


def matrix_vector_multiply(matrix: Sequence[Sequence[Number]], vector: Sequence[Number]) -> Vector:
    """Multiplica uma matriz por um vetor."""
    if not matrix:
        raise ValueError("A matriz nao pode ser vazia.")
    if len(matrix[0]) != len(vector):
        raise ValueError("As dimensoes sao incompativeis para multiplicacao.")

    return [dot_product(row, vector) for row in matrix]


def normalize_vector(vector: Sequence[Number]) -> Vector:
    """Retorna o vetor normalizado; o vetor nulo permanece nulo."""
    vector_norm = norm(vector)
    if vector_norm == 0:
        return [0.0 for _ in vector]
    return [float(value) / vector_norm for value in vector]


def power_iteration(
    matrix: Sequence[Sequence[Number]],
    max_iter: int = 100,
    tolerance: float = 1e-6,
) -> tuple[float, Vector]:
    """Aproxima o autovalor dominante e seu autovetor pelo metodo da potencia."""
    validate_square_matrix(matrix)
    if max_iter <= 0:
        raise ValueError("max_iter deve ser positivo.")
    if tolerance <= 0:
        raise ValueError("tolerance deve ser positivo.")

    size = len(matrix)
    eigenvector = normalize_vector([1.0] * size)
    eigenvalue = 0.0

    for _ in range(max_iter):
        previous_eigenvalue = eigenvalue
        multiplied = matrix_vector_multiply(matrix, eigenvector)
        eigenvector = normalize_vector(multiplied)
        eigenvalue = dot_product(eigenvector, multiplied)

        if abs(eigenvalue - previous_eigenvalue) < tolerance:
            break

    return eigenvalue, eigenvector
