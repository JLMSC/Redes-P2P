"""Arquivo responsável pela exceção customizada relacionada
à incompatibilidade de arquivo de entrada."""

class NonJSONFileFound(Exception):
    """Exceção lançada quando o arquivo de entrada é
    incompatível, ou seja, não é .json."""
