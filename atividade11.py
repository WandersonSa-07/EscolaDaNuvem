"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

temp = input("Informe a temperatura: ")
temp = float(temp)

unidade = input("Digite a unidade de original (C, F ou K): ")
unidade_convertida = input("Digite a unidade que ela deve ser convertida (C, F ou K): ")

resultado = 0

if unidade == "C" and unidade_convertida == "F":
    resultado = (temp * 9/5) + 32
elif unidade == "C" and unidade_convertida == "K":
    resultado = temp + 273.15
elif unidade == "F" and unidade_convertida == "C":
    resultado = (temp - 32) * 5/9
elif unidade == "F" and unidade_convertida == "K":
    resultado = (temp - 32) * 5/9 + 273.15
elif unidade == "K" and unidade_convertida == "C":
    resultado = temp - 273.15
elif unidade == "K" and unidade_convertida == "F":
    resultado = (temp - 273.15) * 9/5 + 32
else:
    resultado = temp # Se as unidades forem iguais

print("A temperatura convertida é:")
print(resultado)
