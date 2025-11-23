"""
2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo
(lê-se igual de trás para frente, ignorando espaços e pontuação). 
Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""

def verificar_palindromo(texto):
    # Converte para minúsculas para comparar igual ('A' igual a 'a')
    texto_limpo = texto.lower()
    
    # Remove espaços e pontuações comuns
    texto_limpo = texto_limpo.replace(" ", "")
    texto_limpo = texto_limpo.replace(",", "")
    texto_limpo = texto_limpo.replace(".", "")
    texto_limpo = texto_limpo.replace("!", "")
    texto_limpo = texto_limpo.replace("?", "")
    texto_limpo = texto_limpo.replace("-", "")

    # Verifica se o texto é igual ao seu inverso
    if texto_limpo == texto_limpo[::-1]:
        return True
    else:
        return False

#Parte de interação com o usuário
print("Verificador de Palíndromo ")
frase_usuario = input("Digite uma palavra ou frase: ")

resultado = verificar_palindromo(frase_usuario)

if resultado == True:
    print("Sim")
else:
    print("Não")