"""
1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).
"""

# Entrada de dados
num1 = input("Digite o primeiro número: ")
num1 = float(num1)

operacao = input("Digite a operação (+, -, *, /): ")

num2 = input("Digite o segundo número: ")
num2 = float(num2)

resultado = 0

if operacao == "+":
    resultado = num1 + num2
    print("O resultado é:", resultado)
elif operacao == "-":
    resultado = num1 - num2
    print("O resultado é:", resultado)
elif operacao == "*":
    resultado = num1 * num2
    print("O resultado é:", resultado)
elif operacao == "/":
    # Verificando se é uma divisão por zero para não dar erro
    if num2 != 0:
        resultado = num1 / num2
        print("O resultado é:", resultado)
    else:
        print("Divisão por zero não é permitida.")
else:
    print("Operação inválida.")