"""Pacote responsável pela junção das buscas 
por recursos em uma topologia."""

# Responsável pela execução das buscas.
from .execute import execute

# Indica o que está disponível para uso no pacote.
__all__: list[str] = [
    'execute',
]
