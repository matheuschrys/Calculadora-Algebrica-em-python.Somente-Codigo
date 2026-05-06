# Calculadora Algébrica em Python

Projeto reorganizado como um pacote Python para operações básicas de álgebra linear, com funções reutilizáveis, interface de linha de comando e testes automatizados.

## Estrutura

```text
.
├── README.md
├── pyproject.toml
├── src/
│   └── calculadora_algebra/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── matrices.py
│       └── vectors.py
├── tests/
│   ├── test_matrices.py
│   └── test_vectors.py
└── trabalho_de_algebra_linear_chrys.ipynb
```

## Funcionalidades

- Soma e subtração de vetores.
- Produto interno.
- Norma de vetor.
- Distância euclidiana.
- Multiplicação matriz-vetor.
- Aproximação do autovalor dominante e autovetor associado pelo método da potência.

## Como executar

Execute a calculadora interativa com:

```bash
PYTHONPATH=src python -m calculadora_algebra
```

Também é possível instalar o projeto em modo editável:

```bash
python -m pip install -e .
calculadora-algebra
```

## Como usar as funções

```python
from calculadora_algebra import add_vectors, dot_product, power_iteration

print(add_vectors([1, 2], [3, 4]))
print(dot_product([1, 2, 3], [4, 5, 6]))
print(power_iteration([[2, 0], [0, 3]]))
```

## Testes

```bash
PYTHONPATH=src pytest
```

O notebook original foi mantido para consulta, mas a lógica principal agora fica nos módulos dentro de `src/calculadora_algebra`.
