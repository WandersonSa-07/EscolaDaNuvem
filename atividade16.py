"""
4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.
"""

print("Digite números inteiros.\nDigite 0 para encerrar.")

pares = 0
impares = 0

while True:
    numero = input("Digite um número: ")
    numero = int(numero)

    if numero == 0:
        break # Sai do loop

    # O resto da divisão por 2 diz se é par ou ímpar
    if numero % 2 == 0:
        print("Este número é PAR")
        pares = pares + 1
    else:
        print("Este número é ÍMPAR")
        impares = impares + 1

print("Total de números Pares digitados:", pares)
print("Total de números Ímpares digitados:", impares)
