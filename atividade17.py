"""
1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros:
a - valor_conta (float): O valor total da conta
b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
c - retorna: float: O valor da gorjeta calculada
"""

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta baseado no total e na porcentagem.
    """
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

#Parte de interação com o usuário
print("=== Calculadora de Gorjeta ===")

entrada_valor = input("Digite o valor total da conta (R$): ")
valor = float(entrada_valor)

entrada_porcentagem = input("Digite a porcentagem da gorjeta: ")
porcentagem = float(entrada_porcentagem)

# Chama a função criada acima
valor_da_gorjeta = calcular_gorjeta(valor, porcentagem)

print(f"O valor da gorjeta é: R$ {valor_da_gorjeta:.2f}")
print(f"Total a pagar: R$ {valor + valor_da_gorjeta:.2f}")
