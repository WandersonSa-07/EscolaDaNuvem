"""
3 -  Crie um programa que leia um arquivo  informado pelo usuário,
percorrendo cada linha do arquivo e a exibe na tela, caso o arquivo não seja encontrado,
mostre uma mensagem de erro.
"""

import csv

nome_arquivo = input("Informe o nome do arquivo: ")

try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas =  arquivo.readlines()
        for linha in linhas:
            print(f"{linha}")

except Exception as erro:
    print("FALHA AO LER O ARQUIVO")
    print(f"Erro: {erro}")
