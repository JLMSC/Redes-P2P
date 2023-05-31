"""Arquivo responsável pela exceção customizada relacionada
à falta de vizinhos de um nó em uma topologia."""

class MissingNodeNeighbors(Exception):
    """Exceção lançada quando nenhum vizinho é
    informado para um nó, em uma topologia, durante
    a criação da topologia."""
