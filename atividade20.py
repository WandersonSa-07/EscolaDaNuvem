"""
4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.
"""
from datetime import date

# Pedindo a data de nascimento
print("Digite sua data de nascimento:")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

# Cria objetos de data
data_nascimento = date(ano, mes, dia)
data_hoje = date.today() # Pega a data atual do sistema automaticamente

# Calcula a diferença
diferenca = data_hoje - data_nascimento

# Exibe o resultado
# .days extrai apenas o número de dias do resultado
print(f"Você está vivo há aproximadamente {diferenca.days} dias.")