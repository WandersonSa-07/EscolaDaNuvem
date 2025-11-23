"""1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais."""

valor = input("Insira o valor em reais: ")
valor = float(valor)

dolar = valor / 5.29
euro = valor / 6.13

print(f"Valor em dolar: {dolar:.2f}")
print(f"Valor em euro: {euro:.2f}")
