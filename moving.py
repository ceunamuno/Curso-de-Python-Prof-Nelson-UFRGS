'''Programa Organizador de Arquivos
Requisitos: Este programa move os arquivos com extensão xlsx e docx para as pastas "planilhas" e "documentos".
Autor: César A. Del Lama de Unamuno
Prof. Dr. Nelson Seixas
Data: 25-11-2022
versão:3.11.0'''

#movendo os arquivos para as pastas "documentos" e "planilhas"
import shutil
import os

def arq():
    arquivos = os.listdir()
    for arquivo in arquivos:
        if '.xlsx' in arquivo:
            shutil.move(arquivo, f'./planilhas/{arquivo})')
        elif 'docx' in arquivo:
            shutil.move(arquivo, f'./documentos/{arquivo}')
    return
arq()

