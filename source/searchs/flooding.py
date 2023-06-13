"""Arquivo responsável pela busca por inundação."""

from typing import Any

def flooding(node: Any, resource: str, ttl: int) -> None:
    """Aplica o algoritmo de busca por inundação.
     
    Parte do nó de origem 'node', buscando pelo
    recurso 'resource', podendo a busca ser limitada
    pelo Time To Live (TTL).

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
    # A lista dos nós (FIFO) a ser visitados.
    # * 1. O nó a ser visitado; 2. O TTL do nó a ser visitado; 3. O caminho.
    queue: list[tuple[Any, int]] = [(node, ttl, [node])]
    # Os nós que já foram visitados.
    visited_nodes: set[Any] = set()

    while queue:
        current_node, current_ttl, current_path = queue.pop(0)
        visited_nodes.add(current_node)

        # Recurso foi encontrado!
        if resource in current_node.resources:
            print(
                f'\nO recurso {resource} FOI' +\
                f' encontrado no nó {current_node.node_id}!' +\
                '\n\t`--> Caminho: ' +\
                ' -> '.join(n.node_id for n in current_path) +\
                f'\n\t`--> Qntd. de mensagens trocadas: {messages_count}' +\
                f'\n\t`--> Qntd. de nós envolvidos: {len(visited_nodes)}'
            )
            resource_found = True
            # ! current_path ta com o caminho da origem até o nó com o recurso.
            break

        neighbors: set[Any] = current_node.neighbors
        for neighbor in neighbors:
            # Ignora os nós já visitados e que tenham TTL > 0
            if current_ttl > 0:
                messages_count += 1
                if neighbor not in visited_nodes and current_ttl > 0:
                    queue.append(
                        (neighbor, current_ttl - 1, current_path + [neighbor])
                    )
                    visited_nodes.add(neighbor)
                    # messages_count += 1

    # Caso o recurso não seja encontrado.
    if not resource_found:
        print(
            f'\nO recurso {resource} NÃO foi encontrado.' +\
            f'\n\t`--> Qntd. de mensagens trocadas: {messages_count}' +\
            f'\n\t`--> Qntd. de nós envolvidos: {len(visited_nodes)}'
        )
