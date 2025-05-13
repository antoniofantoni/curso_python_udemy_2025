# valores de 0 a 10 que sejam menores que 4 usando for  
lista = []
for i in range(10): 
  if i < 4:
    print(i)
#usando list comprehension
lista = [i for i in range(10) if i < 4]
print(lista)

