import os

def fazerUpload(arquivo):
    if arquivo is not None:
        nome = arquivo.name
        partes = nome.split('.')
        extencao = partes[1]

    if extencao != "xlsx":
        return 'Formato de arquivo inválido.'
    else:
        caminho = os.path.join("uploads", "planilha.xlsx")
        with open(caminho, 'wb') as file:
            file.write(arquivo.getbuffer())           
        return 'Arquivo enviado com sucesso!'
    

