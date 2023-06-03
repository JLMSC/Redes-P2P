"""Arquivo responsável pela execução, com métricas,
de um algoritmo de busca."""

from functools import wraps
from typing import Callable

# Exceções.
from exceptions import InvalidParam
from exceptions import InvalidSearchAlgorithm

# Busca por inundação.
from .flooding import flooding
from .informed_flooding import informed_flooding

# Busca por passeio aleatório.
from .random_walk import random_walk
from .informed_random_walk import informed_random_walk

# * Buscas disponíveis para uso.
AVAILABLE_SEARCH_ALGORITHMS: dict[str, Callable] = {
    'flooding': flooding,
    'random_walk': random_walk,
    'informed_flooding': informed_flooding,
    'informed_random_walk': informed_random_walk
}

# TODO: Implementar o wrapper.
def metrics(func: Callable) -> Callable:

    @wraps(wrapped=func)
    def wrapper(algorithm: str, **kwargs) -> None:
        # FIXME: Funções tem que retornar as métricas........
        func(algorithm, **kwargs)
        print("TODO: Métricas")

    return wrapper

@metrics
def execute(algorithm: str, **kwargs) -> None:
    """Executa um algoritmo de busca.

    Parameters
    ----------
    algorithm : str
        O nome do algoritmo de busca a ser executado.

    **kwargs: Any
        Os parâmetros necessários para o algoritmo de busca,
        deve conter: node: Any, resource: str, ttl: int (opcional)

    Raises
    ------
    InvalidSearchAlgorithm
        Caso o algoritmo a ser executado seja inválido.
    InvalidParam
        Caso esteja faltando algum parâmetro essencial para o
        funcionamento do algoritmo de busca.
    """
    # Lança uma exceção ao tentar um algoritmo de busca inválido.
    if algorithm not in AVAILABLE_SEARCH_ALGORITHMS:
        raise InvalidSearchAlgorithm(
            f'O algoritmo \'{algorithm}\' fornecido é inválido.'
        )

    # Lança uma exceção caso não seja passado os parâmetros essenciais.
    expected_params: list[str] = ['node', 'resource', 'ttl']
    if any(param not in expected_params for param in kwargs):
        raise InvalidParam(
            f'Está faltando parâmetros para o algoritmo {algorithm}.'
        )

    # Executa o algoritmo de busca.
    AVAILABLE_SEARCH_ALGORITHMS[algorithm](**kwargs)
