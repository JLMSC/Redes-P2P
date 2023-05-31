"""Arquivo responsável pela validação dos
campos/opções do arquivo de entrada."""

from typing import Any

# Exceções
from exceptions import InvalidOptionInInputFile

# * Os campos que serão aceitos no .json.
_VALID_FIELDS: list[str] = [
    'num_nodes',
    'min_neighbors',
    'max_neighbors',
    'resources',
    'edges',
]

def validate_options(options: Any) -> bool:
    """Valida os campos/opções dos arquivos de entrada.

    Pega a diferença entre os campos/opções válidas e os
    campos/opções do arquivo de entrada, se nenhuma opção
    restar na diferença, significa que todas os campos/opções
    são válidos.

    Parameters
    ----------
    options : Any
        Os campos/opções do arquivo de entrada.

    Returns
    -------
    bool
        Se os campos/opções do arquivo de entrada são válidos.

    Raises
    ------
    InvalidOptionInInputFile
        Caso haja algum campo/opção inválida no arquivo de entrada.
    """
    # Extrai os valores distintos entre 'keys' e '_VALID_FIELDS'.
    options_diff: set[Any] = set(options) - set(_VALID_FIELDS)

    # Lança uma exceção caso haja uma opção inválida no arquivo de entrada.
    if len(options_diff) > 0:
        raise InvalidOptionInInputFile(
            'Os seguintes campos do arquivo de entrada: ' +\
            ', '.join(opt for opt in options_diff) +\
            '\nnão pertencem aos seguintes campos aceitos: ' +\
            ', '.join(opt for opt in _VALID_FIELDS)
        )
    return True
