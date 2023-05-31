"""Arquivo responsável pela exceção customizada relacionada
à falta de recursos de um nó em uma topologia."""

class MissingNodeResources(Exception):
    """Exceção lançada quando nenhum recurso é
    passado para um nó, em uma topologia, durante
    a criação da topologia."""
