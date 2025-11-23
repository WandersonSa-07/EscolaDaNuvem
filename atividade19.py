"""
3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.
"""

print(" Calculadora de Desconto ")

# 1. Pedindo os valores
preco_original = float(input("Digite o preço do produto: R$ "))
porcentagem_desconto = float(input("Digite a porcentagem de desconto (%): "))

# 2. Calculando o desconto
valor_do_desconto = preco_original * (porcentagem_desconto / 100)

# 3. Preço final
preco_final = preco_original - valor_do_desconto

# 4. Exibindo
print("\n \n")
print(f"Valor original: R$ {preco_original:.2f}")
print(f"Valor do desconto: R$ {valor_do_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")