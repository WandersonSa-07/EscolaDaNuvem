"""
3 - Crie um programa que consulte informações de um  na API , retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.
"""

import requests

print("Consulta de CEP ")

cep_digitado = input("Digite o CEP (apenas números): ")

# Monta a URL com o CEP digitado
url = f"https://viacep.com.br/ws/{cep_digitado}/json/"

try:
    resposta = requests.get(url)
    dados_cep = resposta.json()
    
    # A ViaCEP retorna {"erro": true} se o CEP não existir
    if "erro" in dados_cep:
        print("Falha: CEP não encontrado.")
    else:
        print("Logradouro:", dados_cep['logradouro'])
        print("Bairro:", dados_cep['bairro'])
        print("Cidade:", dados_cep['localidade'])
        print("Estado:", dados_cep['uf'])

except:
    print("Falha: Erro na conexão ou formato de CEP inválido.")
