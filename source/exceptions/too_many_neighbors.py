"""Arquivo responsável pela exceção customizada relacionada
à quantidade muito grande de vizinhos de um nó, em uma topologia."""

class TooManyNeighbors(Exception):
    """Exceção lançada quando a quantidade de
    vizinhos de um nó, em uma topologia, é muito
    grande."""
