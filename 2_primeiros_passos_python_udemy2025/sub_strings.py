#Slicing
# Slicing é uma técnica para acessar partes de uma string
# String[início:fim:passo]  # O índice de início é inclusivo e o índice de fim é exclusivo
texto = "Python"

print(texto[0:3])  # Pyt
# Pega do índice 0 até o 2 (não incluindo o 3), ou seja, os 3 primeiros caracteres.

print(texto[0:6])  # Python
# Pega do índice 0 até o 5 (não incluindo o 6), ou seja, todos os 6 caracteres.

print(texto[0:])  # Python
# Pega do índice 0 até o final da string, ou seja, toda a string.

print(texto[:3])  # Pyt
# Pega do início até o índice 2 (não incluindo o 3), ou seja, os 3 primeiros caracteres.

print(texto[1:5])  # yth
# Pega do índice 1 até o 4 (não incluindo o 5), ou seja, pega os caracteres nos índices 1, 2, 3, 4.

print(texto[1:6])  # ython
# Pega do índice 1 até o 5 (não incluindo o 6), ou seja, pega os caracteres nos índices 1 a 5.

print(texto[1:])  # ython
# Pega do índice 1 até o final da string, ou seja, pega 'ython'.

#Slice com passo positivo 
# O passo padrão é 1, ou seja, se não for especificado, o Python irá considerar o passo como 1.
# O passo pode ser positivo ou negativo, mas o padrão é positivo.
print("Com passo positivo")

print(texto[::])  # Python
# Pega toda a string, do início até o final, com passo 1 (padrão).
print(texto[::1])  # Python
print(texto[::2])  # Pto
print(texto[::3])  # Phn
print(texto[::4])  # Pn
print(texto[::5])  # P  
# O último caractere é o índice 5, então o passo 5 pega o primeiro caractere e o último.
print(texto[::6])  # Python

numeros = "0123456789"
print(numeros[::2])  # 02468, pega do índice 0 até o final, com passo 2.
print(numeros[1::2])  # 13579, pega do índice 1 até o final, com passo 2.  

#invertendo a string
print(texto[::-1])  # nohtyP, inverte a string sem pular nenhum caractere.
print(numeros[::-2])  # 97531, inverte a string e pega com passo 2.

# métodos de string
texto = "  Python é incrível!  "

print("strip:")
print(texto.strip())        # Remove espaços no início e fim

print("lower:")
print(texto.lower())        # Converte toda a string para minúsculas

print("upper:")
print(texto.upper())        # Converte toda a string para maiúsculas

print("capitalize:")
print(texto.strip().capitalize())   # Primeira letra maiúscula, resto minúsculo

print("title:")
print(texto.title())        # Primeira letra de cada palavra em maiúsculo

print("replace:")
print(texto.replace("incrível", "poderoso"))  # Substitui uma palavra por outra

print("startswith:")
print(texto.startswith("  Py"))  # Verifica se a string começa com esse trecho

print("endswith:")
print(texto.endswith("!  "))     # Verifica se a string termina com esse trecho

print("find:")
print(texto.find("é"))      # Retorna o índice da primeira ocorrência

print("count:")
print(texto.count("i"))     # Conta quantas vezes o caractere aparece

print("split:")
print(texto.split())        # Divide a string em uma lista de palavras

print("join:")
print("-".join(["Python", "é", "massa"]))  # Junta elementos com separador

print("isalpha:")
print(texto.isalpha())      # Verifica se só há letras (retorna False)

print("isdigit:")
print("123".isdigit())      # Verifica se só há dígitos

print("isalpha (abc):")
print("abc".isalpha())      # Verifica se só há letras

print("isalnum (Abc123):")
print("Abc123".isalnum())   # Verifica se há apenas letras e números

print("isupper (abc):")
print("abc".isupper())      # Verifica se todas as letras estão em maiúsculas

print("islower (abc):")
print("abc".islower())      # Verifica se todas as letras estão em minúsculas

print("istitle (abc):")
print("abc".istitle())      # Verifica se está em formato de título

print("istitle (Abc):")
print("Abc".istitle())      # Verifica se está em formato de título

texto = "Python é incrível!"
palavras = texto.split()  # Divide a string em uma lista de palavras
print(palavras)  # ['Python', 'é', 'incrível!'] 
texto_invertido = " ".join(palavras[::-1])  # Inverte a lista de palavras e junta com espaço
print(texto_invertido)  # incrível! é Python

print("join:")
print(" ".join(["Python", "é", "massa"]))  # Junta elementos com separador

texto1 = "arara"
texto2 = "ovo"
texto3 = "python"

palindromo1 = texto1 == texto1[::-1]  # Verifica se é palíndromo
palindromo2 = texto2 == texto2[::-1]  # Verifica se é palíndromo
palindromo3 = texto3 == texto3[::-1]  # Verifica se é palíndromo
print(f"{texto1} é palíndromo? {palindromo1}")  # True  
print(f"{texto2} é palíndromo? {palindromo2}")  # True
print(f"{texto3} é palíndromo? {palindromo3}")  # False
