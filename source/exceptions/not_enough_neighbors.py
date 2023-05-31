"""Arquivo responsável pela exceção customizada relacionada
à quantidade insuficiente de vizinhos de um nó, em uma topologia."""

class NotEnoughNeighbors(Exception):
    """Exceção lançada quando a quantidade de
    vizinhos de um nó, em uma topologia, é 
    insuficiente.
    """
