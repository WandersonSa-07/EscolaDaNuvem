"""
4 -   Crie um programa que leia e escreva arquivos no formato ,
que salve em um dicionário com nome, idade e cidade em um arquivo JSON
e depois leia o mesmo arquivo exibindo os dados, caso o arquivo não
existir ou ocorrer erro ao salvar, mostre uma mensagem de falha.
"""
import json

dados_pessoa = {
    "nome": "Paulo Damasceno",
    "idade": 21,
    "cidade": "Rio Branco"
}

nome_arquivo = "dados_usuario.json"

#Escrevendo o arquivo
print(f"Salvando os dados em '{nome_arquivo}'...")

try:
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados_pessoa, arquivo, ensure_ascii=False, indent=4)

    print("Arquivo salvo!")

except Exception as erro:
    print("Falha ao salvar o arquivo")
    print(f"Erro: {erro}")

#Lendo o arquivo
print("Tentando ler o arquivo")

try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        dados_lidos = json.load(arquivo)

        print("Dados recuperados do arquivo: ")
        print("Nome:", dados_lidos['nome'])
        print("Idade:", dados_lidos['idade'])
        print("Cidade:", dados_lidos['cidade'])

        print("\nConteúdo bruto:", dados_lidos)

except FileNotFoundError:
    print("O arquivo não existe")
except Exception as erro:
    print("Falha ao ler o arquivo")
    print(f"Erro: {erro}")
