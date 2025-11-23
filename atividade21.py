"""
1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e
 que o usuário  também escolha o tamanho da senha  para criar senhas seguras automaticamente.
"""
import random
import string

print("--- Gerador de Senhas ---")

# 1. Definição dos caracteres possíveis
letras = string.ascii_letters  # letras maiusculas e minusculas
numeros = string.digits        # núemros
simbolos = "!@#$%&*-_"         # símbolos escolhidos

# Junta tudo em uma única string gigante
todos_caracteres = letras + numeros + simbolos

# 2. Interação com o usuário
tamanho = input("Qual o tamanho da senha desejada? ")
tamanho = int(tamanho)

# 3. Gerando a senha
senha_gerada = ""

# Repete o processo 'tamanho' vezes
for i in range(tamanho):
    # Escolhe um caractere aleatório da lista de todos
    escolha = random.choice(todos_caracteres)
    senha_gerada = senha_gerada + escolha

print("Sua nova senha é:", senha_gerada)