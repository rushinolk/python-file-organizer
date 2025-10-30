import os
import shutil

path_dir = "E:\\random_dir\\"

mapeamento_extensoes = {
    ".txt":"Documents",
    ".docx":"Documents",
    ".pdf":"Documents",
    ".png":"Imagens",
    ".jpeg":"Imagens",
    ".zip":"Zipados",
    ".rar":"Zipados"
}


for arquivo in os.listdir(path_dir):

    path_completo = os.path.join(path_dir,arquivo)

    if os.path.isfile(path_completo):
        extensao = os.path.splitext(arquivo)
        nome_pasta = mapeamento_extensoes.get(extensao[1],"Outros")
        pasta_destino = os.path.join(path_dir,nome_pasta)
        arquivo_pasta_destino = os.path.join(pasta_destino,arquivo)

        if os.path.exists(pasta_destino) is False:
            os.mkdir(pasta_destino)

        if os.path.exists(arquivo_pasta_destino) is True:
            i = 1
            arquivo_pasta_destino_rn = arquivo_pasta_destino + (f"({i})")
            while True:
                if os.path.exists(arquivo_pasta_destino_rn) is False:
                    os.rename(path_completo,arquivo_pasta_destino_rn)
                    break
                else:
                    i += 1
        else:
            shutil.move(path_completo,pasta_destino)
            print(f"Arquivo: {arquivo} \n Movido com sucesso")
                    




