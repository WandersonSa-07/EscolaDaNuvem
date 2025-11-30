"""
2 - Crie um programa que cria um arquivo  com nome, idade e cidade de algumas pessoas,
que este programa escreva os dados em formato tabular e salva no arquivo escolhido pelo usuário,
caso ocorra um erro ao salvar, mostre uma mensagem de falha.
"""

import csv

dados_pessoas = [
    ["nome", "idade", "cidade"],
    ["Paulo Damasceno", 21, "Acre"],
    ["Ana Beatriz", 23, "Manaus"],
    ["Wanderson", 22, "Campos dos Goytacazes"],
    ["Jéssica", 30, "Rio de Janeiro"],
    ["Igor", 22, "Bahia"]
]

nome_arquivo = input("Informe o nome do arquivo que será salvo: ")


if not nome_arquivo.endswith(".csv"):
    nome_arquivo = nome_arquivo + ".csv"

try:
    with open(nome_arquivo, 'w', encoding='utf-8' ) as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(dados_pessoas)

    print(f"O arquivo '{nome_arquivo}' foi criado com sucesso")

except Exception as erro:
    print("FALHA AO SALVAR O ARQUIVO")
    print(f"Erro: {erro}")

