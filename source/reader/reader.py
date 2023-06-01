"""Arquivo responsável pela leitura de
arquivos de entradas."""

import json

from typing import Any
from os.path import isfile

# Exceções
from exceptions import MissingInputFile
from exceptions import NonJSONFileFound

def read_json_file(file_path: str = "") -> Any:
    """Faz a leitura de um arquivo de entrada .json.

    Verifica, antes, se o arquivo existe no caminho 
    fornecido e, também, se o arquivo é .json, após
    as verificações, um dicionário será retornado.

    Parameters
    ----------
    file_path : str, optional
        O caminho do arquivo de entrada, por padrão ""

    Returns
    -------
    Any
        Um dicionário contendo as informações lida do
        arquivo de entrada.

    Raises
    ------
    MissingInputFile
        Se o arquivo de entrada não for encontrado no
        caminho fornecido.
    NonJSONFileFound
        Se o arquivo de entrada não for .json.
    """
    # Lança uma exceção se o arquivo de entrada não existir.
    if not isfile(path=file_path):
        raise MissingInputFile(
            'O arquivo de entrada não foi encontrado' +\
            f' no diretório {file_path}'
        )

    # Lança uma exceção se o arquivo não for .json.
    if not file_path.endswith('.json'):
        raise NonJSONFileFound(
            f'O arquivo de entrada {file_path}' +\
            ' encontrado não é .json' 
        )

    # Lazy Import.
    # pylint: disable=import-outside-toplevel
    from . import validate_options

    with open(file=file_path, mode='r', encoding='utf-8') as file:
        data: Any = json.load(fp=file)

        # Valida os campos do arquivo de entrada lido.
        validate_options(options=data.keys())

        file.close()
    return data
