"""
2 - Criar um código que registre as notas de alunos e calcular a média da turma.
"""

print("Digite as notas dos alunos. Digite -1 para parar e calcular a média.")

soma_notas = 0
quantidade_alunos = 0

while True:
    nota = input("Digite a nota do aluno: ")
    nota = float(nota)

    if nota == -1:
        break  # Sai do loop quando digita -1

    soma_notas = soma_notas + nota
    quantidade_alunos = quantidade_alunos + 1

# Calcula a média dos alunos
media = soma_notas / quantidade_alunos
print("A média da turma é:", media)
