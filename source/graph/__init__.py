"""Pacote responsável pela junção de topologias, nós e
buscas: informada e passeio aleatório."""

from .network import Network

# Indica o que está disponível para uso no pacote.
__all__: list[str] = [
    'Network',
]
