#set - Estruturas de Dados em Python
# Sets são coleções não ordenadas de elementos únicos, ou seja, não permitem duplicatas.
# Eles são definidos com chaves `{}` e os elementos são separados por vírgulas. 
# Sets são úteis quando você precisa garantir que não haja duplicatas em uma coleção de dados.

# Criando um set com filmes (sem repetições)
filmes = {"Matrix", "Titanic", "Avatar", "Matrix", "Titanic"}

print("Filmes no set:")
print(filmes)  # Elementos duplicados são automaticamente removidos

# Adicionar um novo filme
filmes.add("Forrest Gump")
print("\nApós adicionar 'Forrest Gump':")
print(filmes)

# Tentar adicionar um filme já existente
filmes.add("Avatar")
print("\nTentando adicionar 'Avatar' novamente (não será duplicado):")
print(filmes)

# Remover um filme
filmes.remove("Titanic")
print("\nApós remover 'Titanic':")
print(filmes)

# Verificar se um filme está no set
print("\n'Avatar' está no set?", "Avatar" in filmes)

# Percorrer os filmes (ordem arbitrária)
print("\nFilmes no set:")
for filme in filmes:
    print(filme)
