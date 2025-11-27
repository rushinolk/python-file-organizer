import os
import shutil
import logging


def ensure_directory_exists(destination_path: str) -> None:
    if not os.path.exists(destination_path):
        os.mkdir(destination_path)


def move_rename_source(file_ext:tuple[str,str],destination_path:str,source_path:str) -> None:
    attempt = 0
    while True:
        attempt += 1
        rename_file = file_ext[0] + (f"({attempt})") + file_ext[1]
        path_source_rename = os.path.join(destination_path,rename_file)
        if not os.path.exists(path_source_rename):
            try:
                shutil.move(source_path,path_source_rename)
                logging.info(f"Arquivo: {path_source_rename} \nMovido com sucesso")
                break
            except OSError:
                logging.error("Falha ao renomear arquivo")
                break



def move_source(source:str,source_path:str,destination_path:str) -> None:
    try:
        shutil.move(source_path,destination_path)
        logging.info(f"Arquivo: {source} \n Movido com sucesso")
    except OSError:
        logging.error("Falha ao mover arquivo")

def build_reserved_destination_paths(base_dir:str,map_ext:dict[str,str]) -> list[str]:
    
    path_make_dir = []
    value_map = list(map_ext.values())
    set_folders = set(value_map)
    set_folders.add('Outros')
    set_folders.add('Pastas')


    for name_dir in set_folders:
        path_dir = os.path.join(base_dir,name_dir)
        path_make_dir.append(path_dir)
        
    return path_make_dir


def organize_downloads(base_dir:str) -> None:
    map_ext = {
        ".txt":"Documents",
        ".docx":"Documents",
        ".pdf":"Documents",
        ".png":"Imagens",
        ".jpeg":"Imagens",
        ".mp4":"Videos",
        ".zip":"Zipados",
        ".rar":"Zipados",
        ".xlsx":"Planilhas",
        ".csv":"Planilhas",
        ".exe":"Executaveis"
    }

    exists_folders = build_reserved_destination_paths(base_dir,map_ext)

    for source in os.listdir(base_dir):

        source_path = os.path.join(base_dir,source)

        if os.path.isfile(source_path):
            
            ext = os.path.splitext(source)
            name_dir = map_ext.get(ext[1],"Outros")
            dir_destination_path = os.path.join(base_dir,name_dir)
            source_destination_path = os.path.join(dir_destination_path,source)

            ensure_directory_exists(dir_destination_path)

            if os.path.exists(source_destination_path): 
                move_rename_source(ext,dir_destination_path,source_path)
            else:
                move_source(source,source_path,dir_destination_path)
                        
        # Criar pasta para pastas e move-las 

        elif os.path.isdir(source_path):

            path_folders = os.path.join(base_dir,'Pastas')
            ensure_directory_exists(path_folders)

            if source_path not in exists_folders:
                try:
                    shutil.move(source_path,path_folders)
                    logging.info(f"Pasta: {source_path} Movido com sucesso")
                except OSError:
                    logging.warning(f"Não foi possivel mover a pasta {source_path}")