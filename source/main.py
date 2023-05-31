"""Arquivo principal."""

from reader import read_json_file

def main(file_path: str) -> None:
    """Função principal."""
    read_json_file(file_path=file_path)

if __name__ == '__main__':
    # main(file_path=input('Informe o caminho do arquivo de entrada: '))
    main(file_path='source/input.json')
