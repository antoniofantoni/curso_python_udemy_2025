import pprint

# Dicionário em Python
# dicionario de dados
# # Dicionários são estruturas de dados que armazenam pares de chave-valor. Eles são mutáveis e não ordenados.  
# Dicionários são definidos com chaves `{}` e os pares de chave-valor são separados por vírgulas.
# Parecida com JSON, mas não é a mesma coisa.
#exemplo de dicionário
funcionario_1 = {
  "nome": "Antonio",
  "idade": 30,
  "cidade": "São Paulo",
  "cargo": "Presidente",
  "salario": 100000.00,
  "endereco": {"rua": "Rua das Flores", "numero": 123,"bairro": "Centro","cep": "12345-678"}
}
print(funcionario_1)

# Acessando valores do dicionário por get e por indice
# Acessando valores do dicionário por numero do indice
# Acessando valores do dicionário por chave

print(funcionario_1["nome"]) # Antonio
print(funcionario_1.get("nome")) # Antonio


#buscar chaves somente
print(funcionario_1.keys()) # dict_keys(['nome', 'idade', 'cidade', 'cargo', 'salario', 'endereco'])
#buscar valores somente
print(funcionario_1.values()) # dict_values(['Antonio', 30, 'São Paulo', 'Presidente', 100000.0, {'rua': 'Rua das Flores', 'numero': 123, 'bairro': 'Centro', 'cep': '12345-678'}]) 

#buscar chaves e valores juntos
print(funcionario_1.items()) # dict_items([('nome', 'Antonio'), ('idade', 30), ('cidade', 'São Paulo'), ('cargo', 'Presidente'), ('salario', 100000.0), ('endereco', {'rua': 'Rua das Flores', 'numero': 123, 'bairro': 'Centro', 'cep': '12345-678'})])  

# Adicionando novos valores ao dicionário
funcionario_1["telefone"] = "11 99999-9999" # Adicionando um novo valor ao dicionário
funcionario_1["cargo"] = "Diretor" # Alterando o valor de um valor existente no dicionário
funcionario_1.update({"cargo": "Diretor"}) # Alterando o valor de um valor existente no dicionário com update
funcionario_1.pop("cargo") # Removendo um valor do dicionário
funcionario_1.popitem() # Removendo o último valor do dicionário
funcionario_1.clear() # Limpando o dicionário

# Dicionário aninhado (dicionário dentro de dicionário)
funcionario_1 = {
  "nome": "Antonio",
  "idade": 30,
  "cidade": "São Paulo",
  "cargo": "Presidente",
  "salario": 100000.00,
  "endereco": {"rua": "Rua das Flores", "numero": 123,"bairro": "Centro","cep": "12345-678"}
} 

print("@@@@@@@@@")
pp = pprint.PrettyPrinter(depth=4) # Indentação de 4 espaços
pp.pprint(funcionario_1) # Imprimindo o dicionário com indentação de 4 espaços

# Acessando valores do dicionário aninhado
print(funcionario_1["endereco"]["rua"]) # Rua das Flores
 
