"""Arquivo responsável pela definição e 
criação de uma topologia."""

from random import choice
from typing import Any, Union

# Buscas.
from searchs import execute

# Exceções customizadas.
from exceptions import NodeIDNotFound
from exceptions import TooManyNeighbors
from exceptions import NotEnoughNeighbors
from exceptions import MissingNodeResources
from exceptions import MissingNodeNeighbors
from exceptions import NetworkIsPartitioned

class Node:
    """Representa um nó em uma topologia."""
    node_id: str
    resources: set[str]
    neighbors: set['Node']

    def __init__(self, node_id: str) -> None:
        self.node_id = node_id
        self.resources = set()
        self.neighbors = set()

class Network:
    """Representa uma topologia de um rede P2P."""
    nodes: set[Node]
    num_nodes: int
    min_neighbors: int
    max_neighbors: int

    def __init__(self, data_info: Any) -> None:
        # Atribui os valores lidos do arquivo de entrada.
        self.num_nodes = data_info['num_nodes']
        self.min_neighbors = data_info['min_neighbors']
        self.max_neighbors = data_info['max_neighbors']

        # Cria os nós (baseia-se na qntd. limite do arquivo de entrada).
        self.nodes = set()
        self.__add_all_nodes()

        # Adiciona os recursos.
        data_resources: Any = data_info['resources']
        for node_id in data_resources:
            self.add_resource(
                node_id=node_id,
                resources=data_resources[node_id]
            )

        # Adiciona os vizinhos.
        data_neighbors: Any = data_info['edges']
        for node_id in data_neighbors:
            self.add_edge(
                node_id=node_id,
                neighbors=data_neighbors[node_id]
            )

    def __add_all_nodes(self) -> None:
        """Adiciona todos os nós necessários a topologia.

        Itera sobre a quantidade total de nós do arquivo
        de entrada, adicionando um por um à topologia.
        """
        for node_id in range(1, self.num_nodes + 1):
            self.nodes.add(
                Node(
                    node_id=f'n{node_id}'
                )
            )

    def is_partitioned(self) -> bool:
        """Verifica se a topologia atual está particionada.

        Basicamente realiza um Breadth-First Search (BFS), em
        um nó qualquer da topologia, se a partir deste nó, for
        possível visitar todos os outros nós, a topologia não
        está particionada.

        Returns
        -------
        bool
            Verdadeiro se a topologia estiver particionada,
            Falso caso contrário.
        """
        # Escolhe um nó inicial qualquer.
        start_node: Node = choice(seq=list(self.nodes))
        # Os nós que já foram visitados.
        visited_nodes: set[Node] = set()

        queue = [start_node]
        while queue:
            # Remove o nó atual da fila e adiciona-o aos visitados.
            current_node = queue.pop(0)
            visited_nodes.add(current_node)

            # Visita os nós vizinhos do nó atual se eles não foram visitados.
            node_neighbors = current_node.neighbors
            for neighbor in node_neighbors:
                if neighbor not in visited_nodes:
                    queue.append(neighbor)

        return len(visited_nodes) != self.num_nodes

    def check_network(self) -> None:
        """Faz a checagem da topologia, verificando se
        está bem estruturada.

        Raises
        ------
        MissingNodeNeighbors
            Caso algum nó não tenha vizinhos.
        NotEnoughNeighbors
            Caso algum nó não tenha vizinhos o suficiente.
        TooManyNeighbors
            Caso algum nó tenha muitos vizinhos.
        NetworkIsPartitioned
            Caso a topologia esteja particionada.
        """
        for node in self.nodes:
            # Lança uma exceção se não houver vizinhos para o nó atual.
            if len(node.neighbors) == 0:
                raise MissingNodeNeighbors(
                    f'Durante a checagem da topologia, o Nó {node.node_id},' +\
                    ' não possui nenhum vizinho.'
                )

            # Lança uma exceção se a qntd. de vizinhos não for suficiente.
            if len(node.neighbors) < self.min_neighbors:
                raise NotEnoughNeighbors(
                    f'Durante a checagem da topologia, o Nó {node.node_id},' +\
                    ' não possui vizinhos suficientes,' +\
                    f' possuindo {len(node.neighbors)} vizinhos,' +\
                    ' o limite definido no arquivo de entrada' +\
                    f' é de {self.min_neighbors}.'
                )

            # Lança uma exceção se a qntd. de vizinhos for muito grande.
            if len(node.neighbors) > self.max_neighbors:
                raise TooManyNeighbors(
                    f'Durante a checagem da topologia, o Nó {node.node_id},' +\
                    ' possui muitos vizinhos,' +\
                    f' possuindo {len(node.neighbors)} vizinhos,' +\
                    ' o limite definido no arquivo de entrada' +\
                    f' é de {self.max_neighbors}.'
                )

            # Lança uma exceção se a topologia conter particionamento.
            if self.is_partitioned():
                raise NetworkIsPartitioned(
                    'Durante a checagem da topologia,' +\
                    ' foi notado a existência de particionamento em algum nó.'
                )

    def add_node(self, node_id: int) -> None:
        """Adiciona um único nó à topologia."""
        self.nodes.add(
            Node(
                node_id=f'n{node_id}'
            )
        )

    def add_edge(self, node_id: str, neighbors: set[str]) -> None:
        """Adiciona um ou mais vizinhos a um nó.

        Faz a busca pelo nó, através de seu id, e adiciona um
        ou mais vizinhos a ele, o mesmo processo é repetido
        para os nós vizinhos, adicionando uma conexão bidirecional.

        Parameters
        ----------
        node_id : str
            O ID do nó a ser adicionado novos recursos.
        neighbors : set[str]
            Os vizinhos a serem adicionados ao nó.

        Raises
        ------
        MissingNodeNeighbors
            Se nenhum vizinho for passado para o nó.
        NodeIDNotFound
            Caso o nó não seja encontrado pelo id fornecido na topologia,
            conta tanto para o nó no qual será adicionado um ou mais vizinhos
            como para os próprios vizinhos.
        """
        if (node := self.find_node_by_id(node_id=node_id)) is not None:
            # Itera sobre os vizinhos fornecidos, adicionando
            # conexão bidirecional.
            for neighbor_id in neighbors:
                if neighbor := self.find_node_by_id(node_id=neighbor_id):
                    node.neighbors.add(neighbor)
                    neighbor.neighbors.add(node)
                else:
                    # Lança uma exceção se o nó vizinho ao nó atual
                    # não for encontrado, pelo id fornecido, na topologia.
                    raise NodeIDNotFound(
                        f'O nó vizinho de {node_id}, de id {node_id},' +\
                        ' não foi encontrado na topologia.'
                    )
        else:
            # Lança uma exceção se o nó não for encontrado, pelo id fornecido,
            # na topologia.
            raise NodeIDNotFound(
                f'O nó de id {node_id},' +\
                ' não foi encontrado na topologia.'
            )

    def add_resource(self, node_id: str, resources: set[str]) -> None:
        """Adiciona um ou mais recursos a um nó.

        Faz a busca pelo nó, através de seu id, e adiciona um
        ou mais recursos a ele.

        Parameters
        ----------
        node_id : str
            O ID do nó a ser adicionado novos recursos.
        resources : set[str]
            Os recursos a serem adicionados ao nó.

        Raises
        ------
        MissingNodeResources
            Se nenhum recurso for passado para o nó.
        NodeIDNotFound
            Caso o nó não seja encontrado pelo id fornecido na topologia.
        """
        if (node := self.find_node_by_id(node_id=node_id)) is not None:
            # Lança uma exceção se não houver recursos para o nó atual.
            if len(resources) == 0:
                raise MissingNodeResources(
                    f'Durante a adição de recursos ao Nó {node_id},' +\
                    ' nenhum recurso foi fornecido.'
                )

            # Adiciona os recursos ao nó.
            for resource in resources:
                node.resources.add(resource)
        else:
            # Lança uma exceção se o nó não for encontrado, pelo id fornecido,
            # na topologia.
            raise NodeIDNotFound(
                f'O nó de id {node_id},' +\
                ' não foi encontrado na topologia.'
            )

    def find_node_by_id(self, node_id: str) -> Union[Node, None]:
        """Busca por um nó, em uma topologia, pelo seu id.

        Parameters
        ----------
        node_id : str
            O id do nó a ser procurado na topologia.

        Returns
        -------
        Union[Node, None]
            O nó, caso seja encontrado, ou nada.
        """
        for node in self.nodes:
            if node.node_id == node_id:
                return node
        return None

    def run_search(self) -> None:
        """Executa algum algoritmo de busca na topologia atual."""
        print('Algoritmos de busca disponíveis:' +\
              '\n\t1- \'flooding\', \'informed_flooding\'' +\
              '\n\t2- \'random_walk\', \'informed_random_walk\'' +\
              '\n')
        # O algoritmo de busca a ser usado.
        algorithm: str = input('[ALGORITMO?] Informe o NOME algoritmo: ')
        # O nó de partida.
        node: Node = self.find_node_by_id(
            node_id=input('[NÓ?] Informe o NÓ de partida: ')
        )
        # O recurso a ser buscado.
        resource: str = input('[RECURSO?] Informe o RECURSO a ser buscado: ')
        # O TTL.
        ttl: int = input('(OPCIONAL) Informe o Time To Live (TTL): ')
        execute(algorithm=algorithm, node=node, resource=resource, ttl=ttl)
