"""Arquivo responsável pela criação de nós e topologias."""

from typing import Type, Any

# Exceções customizadas.
from exceptions import TooManyNeighbors
from exceptions import NotEnoughNeighbors
from exceptions import MissingNodeResources
from exceptions import MissingNodeNeighbors

# TODO: Separar em outro pacote, vai incluir as buscas.

# ? Falta algo? (Cache talvez.)
class Node:
    """Representa um Nó em uma Topologia."""
    node_id: str
    resources: set[str]
    neighbors: set['Node']

    def __init__(
            self,
            node_id: str,
            resources: set[str],
            neighbors: set['Node']
        ) -> None:
        # Lança uma exceção se não houver recursos para o nó atual.
        if len(resources) == 0:
            raise MissingNodeResources(
                f'Durante a criação do Nó {node_id},' +\
                'nenhum recurso foi fornecido.'
            )

        # Lança uma exceção se não houver vizinhos para o nó atual.
        if len(neighbors) == 0:
            raise MissingNodeNeighbors(
                f'Durante a criação do Nó {node_id},' +\
                'nenhum vizinho foi fornecido.'
            )

        # Lança uma exceção se a qntd. de vizinhos não for suficiente.
        if len(neighbors) < Topology.min_neighbors_allowed():
            raise NotEnoughNeighbors(
                f'Durante a criação do Nó {node_id},' +\
                'a quantidade de vizinhos não é suficiente.'
            )

        # Lança uma exceção se a qntd. de vizinhos for muito grande.
        if len(neighbors) > Topology.max_neighbors_allowed():
            raise TooManyNeighbors(
                f'Durante a criação do Nó {node_id},' +\
                'a quantidade de vizinhos é muito grande.'
            )

        # Cria um nó.
        self.node_id = node_id
        self.resources = resources
        self.neighbors = neighbors


# TODO: Implementar.
class Topology:
    """Representa a topologia de uma Rede P2P."""
    nodes: set[Node]

    # TODO: Tirar '_static'?
    # Atributos estáticos.
    _static_num_nodes: int
    _static_min_neighbors: int
    _static_max_neighbors: int

    # TODO: Implementar.
    def __init__(self, data_info: Any) -> None:
        # Atribui os valores essenciais.
        self._static_num_nodes = data_info['num_nodes']
        self._static_min_neighbors = data_info['min_neighbors']
        self._static_max_neighbors = data_info['max_neighbors']

        # TODO: ISso ai de baixo.
        # ? Tem que iterar com resources e edges ao mesmo tempo. ?
        pass

    @classmethod
    def num_nodes(cls: Type['Topology']) -> int:
        """Obtém a quantidade de nós permitidos na topologia.

        Este valor é obtido através da leitura do arquivo de 
        entrada.

        Parameters
        ----------
        cls : Type['Topology']
            Esta classe.

        Returns
        -------
        int
            A quantidade de nós permitidos na topologia.
        """
        return cls._static_num_nodes

    @classmethod
    def min_neighbors_allowed(cls: Type['Topology']) -> int:
        """Obtém a quantidade mínima de vizinhos que os nós
        devem possuir na topologia.

        Este valor é obtido através da leitura do arquivo de
        entrada.

        Parameters
        ----------
        cls : Type['Topology']
            Esta classe.

        Returns
        -------
        int
            A quantidade mínima de vizinhos que os nós
            devem possuir na topologia.
        """
        return cls._static_min_neighbors

    @classmethod
    def max_neighbors_allowed(cls: Type['Topology']) -> int:
        """Obtém a quantidade máxima de vizinhos que os nós
        devem possuir na topologia.

        Este valor é obtido através da leitura do arquivo de
        entrada.

        Parameters
        ----------
        cls : Type['Topology']
            Esta classe.

        Returns
        -------
        int
            A quantidade máxima de vizinhos que os nós
            devem possuir na topologia.
        """
        return cls._static_max_neighbors
