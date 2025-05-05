# Definição de listas
# Listas são estruturas de dados que podem armazenar múltiplos valores em uma única variável.
# Elas são mutáveis, ou seja, podem ser alteradas após a criação. Listas são definidas com colchetes `[]` e os elementos são separados por vírgulas.
lista_de_frutas = ["maçã", "banana", "laranja", "uva"]
print(lista_de_frutas)  # ['maçã', 'banana', 'laranja', 'uva']  
print(type(lista_de_frutas))  # <class 'list'>
print(len(lista_de_frutas))  # 4, conta o número de elementos na lista
print(lista_de_frutas[0])  # maçã, acessa o primeiro elemento da lista (índice 0)
print(lista_de_frutas[1])  # banana, acessa o segundo elemento da lista (índice 1)
print(lista_de_frutas[2])  # laranja, acessa o terceiro elemento da lista (índice 2)
print(lista_de_frutas[3])  # uva, acessa o quarto elemento da lista (índice 3)
print(lista_de_frutas[-1])  # uva, acessa o último elemento da lista (índice -1)
print(lista_de_frutas[-2])  # laranja, acessa o penúltimo elemento da lista (índice -2) 
print(lista_de_frutas[-3])  # banana, acessa o antepenúltimo elemento da lista (índice -3)
print(lista_de_frutas[-4])  # maçã, acessa o quarto elemento da lista (índice -4)

#### filme matriz lista
filme_matrix = ["Matrix", 1999, "Lana Wachowski", "Keanu Reeves", "Carrie-Anne Moss"]
print(filme_matrix)  # ['Matrix', 1999, 'Lana Wachowski', 'Keanu Reeves', 'Carrie-Anne Moss']
print(type(filme_matrix))  # <class 'list'>
print(filme_matrix[:2]) # # ['Matrix', 1999], acessa os dois primeiros elementos da lista (índices 0 e 1)
print(filme_matrix[2:]) # ['Lana Wachowski', 'Keanu Reeves', 'Carrie-Anne Moss'], acessa os elementos a partir do índice 2 até o final da lista

# Nova Lista de filmes
filmes = ["O Poderoso Chefão", "Interestelar", "Matrix", "Clube da Luta", "Forrest Gump"]

# Exibir todos os filmes
print("Lista de filmes:")
print(filmes)

# Adicionar um novo filme
filmes.append("A Origem")
print("\nApós adicionar 'A Origem':")
print(filmes)

# Remover um filme
filmes.remove("Matrix")
print("\nApós remover 'Matrix':")
print(filmes)

# Buscar se um filme está na lista
filme_busca = "Forrest Gump"
if filme_busca in filmes:
    print(f"\n'{filme_busca}' está na lista.")
else:
    print(f"\n'{filme_busca}' não está na lista.")

# Mostrar quantidade de filmes
print(f"\nTotal de filmes: {len(filmes)}")

# Ordenar a lista em ordem alfabética
filmes.sort()
print("\nFilmes em ordem alfabética:")
print(filmes)

#mostrar os indices dos filmes
for i in range(len(filmes)):
    print(f"Índice {i}: {filmes[i]}")  # Mostra o índice e o filme correspondente 
#copiar a lista
filmes_copia = filmes.copy() # Cria uma cópia da lista de filmes
print("\nCópia da lista de filmes:")
print(filmes_copia)  # Mostra a cópia da lista de filmes
# Adicionar um filme na posição 2
filmes.insert(2, "O Senhor dos Anéis")  # Adiciona "O Senhor dos Anéis" na posição 2 da lista
print("\nApós adicionar 'O Senhor dos Anéis' na posição 2:")

#limpar a lista
filmes.clear()  # Limpa todos os elementos da lista de filmes 
print("\nApós limpar a lista de filmes:")
print(filmes)  # Mostra a lista de filmes após a limpeza

