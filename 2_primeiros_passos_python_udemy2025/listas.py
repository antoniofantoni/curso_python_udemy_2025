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



