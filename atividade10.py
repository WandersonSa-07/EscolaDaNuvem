"""
2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
"""

peso = input("Informe o seu peso em kg: ")
peso = float(peso)

altura = input("Informe a sua altura em metros: ")
altura = float(altura)

IMC = peso / (altura ** 2)

print("Sua classificação é ")
if (IMC < 18.5):
    print("abaixo do peso")
elif ((IMC > 18.5) & (IMC < 25)):
    print("peso normal")
elif ((IMC > ))