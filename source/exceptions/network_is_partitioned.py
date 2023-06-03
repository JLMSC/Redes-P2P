"""Arquivo responsável pela exceção customizada relacioanda
a existência de particionamento em uma topologia."""

class NetworkIsPartitioned(Exception):
    """Exceção lançada quando existe particionamento
    na topologia."""
