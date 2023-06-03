"""Pacote responsável pela criação de topologias e nós;"""

from .network import Network

# Indica o que está disponível para uso no pacote.
__all__: list[str] = [
    'Network',
]
