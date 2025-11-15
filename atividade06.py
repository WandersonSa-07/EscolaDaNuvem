"""
Atividade 2.2
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

preco = 50.00
porcentagem_desconto = 20

desconto = preco * (porcentagem_desconto/100)
compra = preco - desconto

print(f"A compra foi de {compra:.2f} reais, seu desconto foi de {desconto:.2f} reais")

