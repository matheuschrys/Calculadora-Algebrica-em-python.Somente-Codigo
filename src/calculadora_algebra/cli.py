"""Interface de linha de comando da calculadora de algebra linear."""

from collections.abc import Callable

from .matrices import power_iteration
from .vectors import add_vectors, distance, dot_product, norm, subtract_vectors


def read_positive_int(prompt: str) -> int:
    """Le um inteiro positivo a partir do terminal."""
    while True:
        value = input(prompt)
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Digite um numero inteiro positivo.")


def read_float(prompt: str) -> float:
    """Le um numero real a partir do terminal."""
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Digite um numero valido.")


def read_vector(size: int, name: str) -> list[float]:
    """Le um vetor de tamanho fixo."""
    print(f"\nPreenchendo {name} (dimensao {size})")
    return [read_float(f"  Elemento {index + 1}: ") for index in range(size)]


def read_vectors(quantity: int, size: int) -> list[list[float]]:
    """Le varios vetores de mesma dimensao."""
    return [read_vector(size, f"Vetor {index + 1}") for index in range(quantity)]


def read_square_matrix(size: int) -> list[list[float]]:
    """Le uma matriz quadrada."""
    print(f"\nPreenchendo matriz {size}x{size}")
    return [
        [read_float(f"  Elemento ({row + 1}, {column + 1}): ") for column in range(size)]
        for row in range(size)
    ]


def show_vectors(vectors: list[list[float]]) -> None:
    """Exibe os vetores informados."""
    for index, vector in enumerate(vectors, start=1):
        print(f"Vetor {index}: {vector}")


def run_vector_sum() -> None:
    quantity = read_positive_int("Quantidade de vetores: ")
    size = read_positive_int("Dimensao dos vetores: ")
    vectors = read_vectors(quantity, size)
    show_vectors(vectors)
    print(f"Soma: {add_vectors(*vectors)}")


def run_vector_subtraction() -> None:
    quantity = read_positive_int("Quantidade de vetores: ")
    size = read_positive_int("Dimensao dos vetores: ")
    vectors = read_vectors(quantity, size)
    show_vectors(vectors)
    print(f"Subtracao: {subtract_vectors(vectors[0], *vectors[1:])}")


def run_dot_product() -> None:
    size = read_positive_int("Dimensao dos vetores: ")
    first = read_vector(size, "Vetor 1")
    second = read_vector(size, "Vetor 2")
    print(f"Produto interno: {dot_product(first, second)}")


def run_norm() -> None:
    size = read_positive_int("Dimensao do vetor: ")
    vector = read_vector(size, "Vetor")
    print(f"Norma: {norm(vector)}")


def run_distance() -> None:
    size = read_positive_int("Dimensao dos vetores: ")
    first = read_vector(size, "Vetor 1")
    second = read_vector(size, "Vetor 2")
    print(f"Distancia euclidiana: {distance(first, second)}")


def run_power_iteration() -> None:
    size = read_positive_int("Tamanho da matriz quadrada: ")
    matrix = read_square_matrix(size)
    eigenvalue, eigenvector = power_iteration(matrix)
    print(f"Autovalor dominante aproximado: {eigenvalue:.6f}")
    print(f"Autovetor associado aproximado: {[round(value, 6) for value in eigenvector]}")


def build_menu() -> dict[str, tuple[str, Callable[[], None]]]:
    """Monta as opcoes disponiveis na CLI."""
    return {
        "1": ("Soma de vetores", run_vector_sum),
        "2": ("Subtracao de vetores", run_vector_subtraction),
        "3": ("Produto interno", run_dot_product),
        "4": ("Norma de vetor", run_norm),
        "5": ("Distancia euclidiana", run_distance),
        "6": ("Autovalor dominante por metodo da potencia", run_power_iteration),
    }


def main() -> None:
    """Executa a calculadora interativa."""
    menu = build_menu()

    while True:
        print("\nCalculadora de Algebra Linear")
        for key, (description, _) in menu.items():
            print(f"{key}. {description}")
        print("0. Sair")

        option = input("Escolha uma opcao: ").strip()
        if option == "0":
            print("Encerrando calculadora.")
            return

        item = menu.get(option)
        if item is None:
            print("Opcao invalida.")
            continue

        _, action = item
        action()


if __name__ == "__main__":
    main()
