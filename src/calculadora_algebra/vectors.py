"""Operacoes com vetores sem dependencia de bibliotecas externas."""

from math import sqrt
from typing import Iterable, Sequence

Number = int | float
Vector = list[float]


def as_vector(values: Iterable[Number]) -> Vector:
    """Converte um iteravel numerico para uma lista de floats."""
    return [float(value) for value in values]


def validate_same_dimension(*vectors: Sequence[Number]) -> None:
    """Garante que todos os vetores tenham a mesma dimensao."""
    if not vectors:
        raise ValueError("Informe pelo menos um vetor.")

    expected_size = len(vectors[0])
    if expected_size == 0:
        raise ValueError("Vetores vazios nao sao aceitos.")

    for index, vector in enumerate(vectors, start=1):
        if len(vector) != expected_size:
            raise ValueError(
                f"O vetor {index} tem dimensao {len(vector)}, "
                f"mas era esperado {expected_size}."
            )


def add_vectors(*vectors: Sequence[Number]) -> Vector:
    """Soma dois ou mais vetores de mesma dimensao."""
    validate_same_dimension(*vectors)
    return [sum(values) for values in zip(*vectors)]


def subtract_vectors(first: Sequence[Number], *others: Sequence[Number]) -> Vector:
    """Subtrai os demais vetores do primeiro vetor informado."""
    validate_same_dimension(first, *others)
    result = as_vector(first)
    for vector in others:
        result = [current - float(value) for current, value in zip(result, vector)]
    return result


def dot_product(first: Sequence[Number], second: Sequence[Number]) -> float:
    """Calcula o produto interno entre dois vetores."""
    validate_same_dimension(first, second)
    return sum(float(x) * float(y) for x, y in zip(first, second))


def norm(vector: Sequence[Number]) -> float:
    """Calcula a norma euclidiana de um vetor."""
    validate_same_dimension(vector)
    return sqrt(dot_product(vector, vector))


def distance(first: Sequence[Number], second: Sequence[Number]) -> float:
    """Calcula a distancia euclidiana entre dois vetores."""
    validate_same_dimension(first, second)
    differences = subtract_vectors(first, second)
    return norm(differences)
