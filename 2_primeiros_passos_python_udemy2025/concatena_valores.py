name = "Top Gun Maverick"
yearLaunch = 2023
noteMovie = 9.5
planIncluded = False

# Exibindo os tipos de dados de cada variável 1
print("Dados do filme:")
print("Nome do filme:", name)
print("Ano de lançamento:", yearLaunch)  
print("Nota do filme:", noteMovie)
print("Plano incluído:", planIncluded)

# Exibindo os tipos de dados de cada variável 2
print("Dados do filme:", name, yearLaunch, noteMovie, planIncluded)

# Exibindo os tipos de dados de cada variável 3
print("Dados do filme: " + name + " " + str(yearLaunch) + " " + str(noteMovie) + " " + str(planIncluded))

# Exibindo os tipos de dados de cada variável com um print só, usando \n para pular linha e separando por vírgula
print("Dados do filme=>\nNome do filme:", name, "\nAno de lançamento:", yearLaunch, "\nNota do filme:", noteMovie, "\nPlano incluído:", planIncluded)

# Exibindo os tipos de dados de cada variável 4 usando f-string
print(f"Dados do filme: Nome do filme:\n{name}\nAno de lançamento: {yearLaunch}\nNota:{noteMovie}")
if planIncluded:
    print("Plano incluído: Sim")
else:
    print("Plano incluído: Não")