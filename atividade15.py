"""
3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.
"""

senha = input("Crie sua senha: ")

# Critério de tamanho:
tamanho_ok = False
if len(senha) >= 8:
    tamanho_ok = True

# Verificando se tem número:
tem_numero = False
# O loop olha caractere por caractere
for caractere in senha:
    # Verifica se o caractere está na lista de números
    if caractere in "0123456789":
        tem_numero = True

# Resultado
if (tamanho_ok == True) and (tem_numero == True):
    print("Senha válida e segura!")
else:
    print("Senha inválida.")
    if tamanho_ok == False:
        print("- A senha precisa ter 8 ou mais caracteres.")
    if tem_numero == False:
        print("- A senha precisa ter pelo menos um número.")