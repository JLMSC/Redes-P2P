"""Arquivo principal."""

from typing import Any

from graph import Network
from reader import read_json_file

def main(file_path: str) -> None:
    """Função principal."""
    data_read: Any = read_json_file(file_path=file_path)
    network: Network = Network(data_info=data_read)
    network.check_network()

if __name__ == '__main__':
    # main(file_path=input('Informe o caminho do arquivo de entrada: '))
    main(file_path='source/input.json')
