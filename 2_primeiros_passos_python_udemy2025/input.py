numero_inteiro = input("Digite um número inteiro: \n")
print(type(numero_inteiro))  # Mostra o tipo da variável antes da conversão
numero_inteiro = int(numero_inteiro)  # Converte a string para inteiro
print(type(numero_inteiro))  # Mostra o tipo da variável antes da conversão

numero_decimal =input("Digite um número decimal: ")
print(type(numero_decimal))  # Mostra o tipo da variável antes da conversão
numero_decimal = float(numero_decimal)  # Converte a string para float.
print(type(numero_decimal))  # Mostra o tipo da variável antes da conversão

print("\n--- Resultado ---")
print(f"Número inteiro: {numero_inteiro}")
print(f"Número decimal: {numero_decimal}")

