import os
import shutil


def criar_pasta_destino(pasta_destino: str):
    if os.path.exists(pasta_destino) is False:
        os.mkdir(pasta_destino)


def mover_arquivo_rename(extensao:tuple,pasta_destino:str,caminho_origem:str):
    i = 0
    while True:
        i += 1
        rename = extensao[0] + (f"({i})") + extensao[1]
        arquivo_pasta_destino_rename = os.path.join(pasta_destino,rename)
        if os.path.exists(arquivo_pasta_destino_rename) is False:
            shutil.move(caminho_origem,arquivo_pasta_destino_rename)
            print(f"Arquivo: {arquivo_pasta_destino_rename} \nMovido com sucesso")
            break

def mover_arquivo(arquivo:str,arquivo_origen:str,pasta_destino:str):
    shutil.move(arquivo_origen,pasta_destino)
    print(f"Arquivo: {arquivo} \n Movido com sucesso")


def criar_lista_pastas_existentes(path_dir,mapeamento_extensoes):
    caminho_pasta_criada = []

    for extensao in mapeamento_extensoes:
        pasta_criada = mapeamento_extensoes[extensao]
        caminho_pasta = os.path.join(path_dir,pasta_criada)
        if caminho_pasta not in caminho_pasta_criada:
            caminho_pasta_criada.append(caminho_pasta)
        
    return caminho_pasta_criada


if __name__ == '__main__':

    path_dir = "C:\\Users\\arthu\\Downloads\\"
    


    mapeamento_extensoes = {
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

    pastas_existentes = criar_lista_pastas_existentes(path_dir,mapeamento_extensoes)

    for arquivo in os.listdir(path_dir):

        arquivo_origen = os.path.join(path_dir,arquivo)

        if os.path.isfile(arquivo_origen):
            
            extensao = os.path.splitext(arquivo)
            nome_pasta = mapeamento_extensoes.get(extensao[1],"Outros")
            pasta_destino = os.path.join(path_dir,nome_pasta)
            arquivo_pasta_destino = os.path.join(pasta_destino,arquivo)

            criar_pasta_destino(pasta_destino)

            if os.path.exists(arquivo_pasta_destino) is True: 
                mover_arquivo_rename(extensao,pasta_destino,arquivo_origen)
            else:
                mover_arquivo(arquivo,arquivo_origen,pasta_destino)
                        
        # Criar pasta para pastas e move-las 

        elif os.path.isdir(arquivo_origen):

            
            caminho_pasta_pastas = os.path.join(path_dir,'Pastas')

            criar_pasta_destino(caminho_pasta_pastas)

            if arquivo_origen not in pastas_existentes:
                shutil.move(arquivo_origen,caminho_pasta_pastas)