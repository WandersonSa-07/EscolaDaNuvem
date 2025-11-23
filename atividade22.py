"""
2 -   Crie um programa que  acesse a API  para buscar um usuário fictício aleatório.
 exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.
"""
import requests

print(" Buscando Usuário Fictício ")

# URL da API pública
url = "https://randomuser.me/api/"

try:
    # Tenta fazer a conexão
    resposta = requests.get(url)
    
    # Pega os dados no formato JSON
    dados = resposta.json()
    
    # A API retorna uma lista 'results', pega o primeiro item (0)
    usuario = dados['results'][0]
    
    # Extraindo as informações específicas
    primeiro_nome = usuario['name']['first']
    sobrenome = usuario['name']['last']
    email = usuario['email']
    pais = usuario['location']['country']
    
    print(f"Nome: {primeiro_nome} {sobrenome}")
    print(f"E-mail: {email}")
    print(f"País: {pais}")

except:
    # Se der erro de internet ou URL
    print("Falha: Não foi possível conectar à API.")
    