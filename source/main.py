"""Arquivo principal."""

from typing import Any

from graph import Network
from reader import read_json_file

def main(file_path: str) -> None:
    """Função principal."""
    data_read: Any = read_json_file(file_path=file_path)
    network: Network = Network(data_info=data_read)
    network.check_network()

    # TODO: try except!!!!! (se não os raise vão parar o programa.)
    while True:
        print('\n' * 50)
        print('Pressione [Ctrl + C] para sair.\n')
        network.run_search()
        # TODO: Dps de executar um algoritmo, pedir confirmação de entrada p/ continuar.

if __name__ == '__main__':
    main(file_path='source/input.json')
