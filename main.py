import argparse
import os
import logging
import sys 
from src.organizer import organize_downloads

logging.basicConfig(
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - %(message)s', # Formato da mensagem
    datefmt='%Y-%m-%d %H:%M:%S', # Formato da data
    handlers=[
        logging.FileHandler("logs/pipeline.log", mode='a', encoding='utf-8'),
        logging.StreamHandler()            # Também exibe o log no console
    ]
)

def parse_args() -> str: 
    parser = argparse.ArgumentParser(prog="dir-organizer")
    parser.add_argument("-p", 
                        "--path",
                        type=str,
                        default=os.path.join(os.path.expanduser("~"), "Downloads"),
                        help= "Caminho da pasta a ser organizada. Padrão: pasta Downloads do usuário.",)
    args = parser.parse_args()
    return args.path


if __name__ == "__main__":
    path_dir = parse_args()

    if not os.path.isdir(path_dir):
        logging.error("Caminho não encontrado, interrompendo programa")
        sys.exit(1)
    else:
        organize_downloads(path_dir)