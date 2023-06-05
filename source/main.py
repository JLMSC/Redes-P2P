"""Arquivo principal."""

from typing import Any

from graph import Network
from reader import read_json_file

def wait_for_key_press(key: str) -> None:
    """Para temporariamente a execução do programa,
    até que seja 'pressionado' a tecla 'ENTER'.

    Parameters
    ----------
    key : str
        A tecla a ser observada.
    """
    while True:
        key_pressed: str = input()
        if key_pressed == key:
            break

def run(network: Network) -> None:
    """Executa o programa."""
    while True:
        # Limpa a tela.
        print('\n' * 100)
        # Mostra como parar a execução do programa.
        print('Pressione [Ctrl + C | Ctrl + D] para sair.\n')

        network.run_search()

        # Aguarda o 'pressionamento' da tecla 'ENTER' para dar
        # continuidade ao programa.
        print('\nPressione [ENTER] para dar continuidade ao programa.')
        wait_for_key_press(key='')

def main(file_path: str) -> None:
    """Função principal."""
    data_read: Any = read_json_file(file_path=file_path)
    network: Network = Network(data_info=data_read)
    network.check_network()

    try:
        # Executa o programa.
        run(network=network)
    # pylint: disable=broad-exception-caught
    except Exception as excp:
        print(
            f'\t`--> [!] [{type(excp).__name__}] {excp.args[0]}'
        )
    # Aguarda o 'pressionamento' da tecla 'ENTER' para dar
    # continuidade ao programa.
    print('\nPressione [ENTER] para dar continuidade ao programa.')
    wait_for_key_press(key='')
    # Continua a execução do programa.
    run(network=network)

if __name__ == '__main__':
    main(file_path='source/input.json')
