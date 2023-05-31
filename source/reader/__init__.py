"""Pacote responsável pela junção do leitor de
arquivos de entrada."""

from .reader import read_json_file
from .validator import validate_options

# Indica o que está disponível para uso no pacote.
__all__: list[str] = [
    'read_json_file',
    'validate_options',
]
