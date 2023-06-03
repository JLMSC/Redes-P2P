"""Pacote responsável pela junção das exceções
customizadas."""

# Exceções customizadas.
from .node_id_not_found import NodeIDNotFound
from .missing_input_file import MissingInputFile
from .too_many_neighbors import TooManyNeighbors
from .non_json_file_found import NonJSONFileFound
from .not_enough_neighbors import NotEnoughNeighbors
from .missing_node_resources import MissingNodeResources
from .missing_node_neighbors import MissingNodeNeighbors
from .network_is_partitioned import NetworkIsPartitioned
from .invalid_option_in_input_file import InvalidOptionInInputFile

# Indica quais exceções estarão disponíveis para uso no pacote.
__all__: list[str] = [
    'NodeIDNotFound',
    'MissingInputFile',
    'TooManyNeighbors',
    'NonJSONFileFound',
    'NotEnoughNeighbors',
    'MissingNodeResources',
    'MissingNodeNeighbors',
    'NetworkIsPartitioned',
    'InvalidOptionInInputFile',
]
