"""Arquivo responsável pela busca por passeio aleatório informada."""

from typing import Any
from random import shuffle

def informed_random_walk(node: Any, resource: str, ttl: int) -> None:
    """Aplica o algoritmo de busca por passeio aleatório informada.

    Parte do nó de origem 'node', buscando pelo recurso
    'resource', podendo a busca ser limitada pelo
    Time To Live (TTL).

    Parameters
    ----------
    node : Any
        O nó de origem, onde será iniciado a busca.
    resource : str
        O recurso a ser buscado na topologia.
    ttl : int
        O limitador de 'saltos' na busca.
    """
    # Qntd. de mensagens trocadas entre os nós.
    messages_count: int = 0
    resource_found: bool = False
    # Os nós que já foram visitados.
    visited_nodes: set[str] = set()

    def recursive_informed_walk(
            node: Any,
            resource: str,
            ttl: int,
            path: list[Any]
        ) -> None:
        """Algoritmo recursivo da busca por passeio aleatório.

        Parameters
        ----------
        node : Any
            O nó atual a ser visitado.
        resource : str
            O recurso a ser buscado na topologia.
        ttl : int
            O TTL do nó atual.
        path : list[Any]
            O caminho do nó origem até o nó atual.
        """
        nonlocal messages_count, resource_found, visited_nodes

        # Recurso foi encontrado!
        if resource in node.resources:
            print(
                f'\nO recurso {resource} FOI' +\
                f' encontrado no nó {node.node_id}!' +\
                '\n\t`--> Caminho: ' +\
                ' -> '.join(n.node_id for n in path) +\
                f'\n\t`--> Qntd. de mensagens trocadas: {messages_count}' +\
                f'\n\t`--> Qntd. de nós envolvidos: {len(visited_nodes)}'
            )
            resource_found = True
            # Atualiza o cache dos nós da origem até o nó com o recurso.
            for node_path in path:
                node_path.add_cache(node=node, resource=resource)

        # Marca o nó atual como visitado.
        visited_nodes.add(node)

        # Cria uma cópia e randomiza a ordem dos vizinhos.
        neighbors: list[Any] = list(node.neighbors)
        random_neighbors: list[Any] = list(neighbors)
        shuffle(x=random_neighbors)

        for neighbor in random_neighbors:
            # Ignora os nós já visitados e que tenham TTL > 0
            if neighbor not in visited_nodes and ttl > 0:
                messages_count += 1
                # Vai direto para o nó que tem o recurso.
                if neighbor.know_resource(resource=resource):
                    # O nó que contém o recurso (cache).
                    target_node: Any = neighbor.get_node_by_resource(
                        resource=resource
                    )
                    recursive_informed_walk(
                        node=target_node,
                        resource=resource,
                        ttl=ttl - 1,
                        path=path + [target_node]
                    )
                # Caso contrário, visita, aleatoriamente, os vizinhos.
                else:
                    recursive_informed_walk(
                        node=neighbor,
                        resource=resource,
                        ttl=ttl - 1,
                        path=path + [neighbor]
                    )

    recursive_informed_walk(node=node, resource=resource, ttl=ttl, path=[node])

    # Caso o recurso não seja encontrado.
    if not resource_found:
        print(
            f'\nO recurso {resource} NÃO foi encontrado.' +\
            f'\n\t`--> Qntd. de mensagens trocadas: {messages_count}' +\
            f'\n\t`--> Qntd. de nós envolvidos: {len(visited_nodes)}'
        )
