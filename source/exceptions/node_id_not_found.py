"""Arquivo responsável pela exceção customizada relacionada
à busca sem sucesso pelo id de um nó."""

class NodeIDNotFound(Exception):
    """Exceção lançada quando uma busca por um nó,
    através do id de um nó, não é encontrado."""
