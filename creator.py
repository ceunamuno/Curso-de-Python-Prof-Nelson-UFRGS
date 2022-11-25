'''Programa Organizador de Arquivos
Requisitos: Este programa cria as pastas "planilhas" e "documentos".
Autor: César A. Del Lama de Unamuno
Prof. Dr. Nelson Seixas
Data: 25-11-2022
versão:3.11.0'''

#Criando as pastas
import os
def entrada():

    if os.path. exists('documentos') == False:
        os.mkdir('documentos')

    if os.path.exists('planilhas') == False:
        os.mkdir('planilhas')
    return
entrada()


