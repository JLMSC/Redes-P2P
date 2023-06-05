"""Arquivo responsável pela busca por inundação informada."""

from typing import Any

def informed_flooding(node: Any, resource: str, ttl: int) -> None:
    """Aplica o algoritmo de busca por inundação informada.
     
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
            # Atualiza o cache dos nós da origem até o nó com o recurso.
            for node_path in current_path:
                node_path.add_cache(node=current_node, resource=resource)
            break

        neighbors: set[Any] = current_node.neighbors
        for neighbor in neighbors:
            # Ignora os nós já visitados e que tenham TTL > 0
            if neighbor not in visited_nodes and current_ttl > 0:
                messages_count += 1
                visited_nodes.add(neighbor)
                if neighbor.know_resource(resource=resource):
                    # O nó que contém o recurso (cache).
                    target_node: Any = neighbor.get_node_by_resource(
                        resource=resource
                    )
                    queue.insert(
                        0,
                        (target_node, 0, current_path + [target_node])
                    )
                    visited_nodes.add(target_node)
                    break
                else:
                    queue.append(
                        (neighbor, current_ttl - 1, current_path + [neighbor])
                    )

    # Caso o recurso não seja encontrado.
    if not resource_found:
        print(
            f'\nO recurso {resource} NÃO foi encontrado.' +\
            f'\n\t`--> Qntd. de mensagens trocadas: {messages_count}' +\
            f'\n\t`--> Qntd. de nós envolvidos: {len(visited_nodes)}'
        )
