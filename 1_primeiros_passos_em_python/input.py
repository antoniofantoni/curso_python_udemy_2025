# Entrada de um número inteiro
numero_inteiro = int(input("Digite um número inteiro: \n"))

# Entrada de um número float
numero_decimal = float(input("Digite um número decimal: "))


# Entrada de uma frase com quebra de linha inserida como '\n'
frase = input("Digite uma frase com '\\n' para quebrar linhas (ex: linha1\\nlinha2): ")

# Substitui as ocorrências de '\n' (texto) pela quebra de linha real
frase_formatada = frase.replace("\\n", "\n")

# Exibindo os dados capturados
print("\n--- Resultado ---")
print(f"Número inteiro: {numero_inteiro}")
print(f"Número decimal: {numero_decimal}")
print("Frase digitada com quebras de linha:")
print(frase_formatada)