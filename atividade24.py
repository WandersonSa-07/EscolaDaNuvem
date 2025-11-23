"""
4 - Crie um programa que realize consultas a  em relação ao Real (BRL) usando a API mostre valor atual,
 máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.
"""
import requests

print("--- Cotação de Moedas (Diagnóstico) ---")
print("Tente: USD, EUR, BTC")

moeda = input("Digite a moeda: ").upper()

# Prevenção simples: avisa se tentar converter Real para Real
if moeda == "BRL":
    print("Aviso: A API converte moedas estrangeiras para Real.")
    print("Para testar, use USD (Dólar) ou EUR (Euro).")
else:
    url = f"https://awesomeapi.com.br/last/{moeda}-BRL"
    print(f"Tentando conectar em: {url}")

    try:
        resposta = requests.get(url)
        
        # Mostra o código de status para sabermos o que aconteceu (200 é OK, 404 é não encontrado)
        print(f"Status da conexão: {resposta.status_code}")

        if resposta.status_code == 200:
            dados = resposta.json()
            info_moeda = list(dados.values())[0]
            
            nome = info_moeda['name']
            valor = info_moeda['bid']
            
            print(f"Sucesso! {nome}: R$ {valor}")
        else:
            print("Erro: A moeda não foi encontrada na API.")

    except Exception as erro_detalhado:
        # Aqui ele vai imprimir o erro técnico real
        print("--- OCORREU UM ERRO TÉCNICO ---")
        print(erro_detalhado)