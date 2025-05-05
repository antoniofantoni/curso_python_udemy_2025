"""
Tuplas são criadas com ( ) e lista com [ ]
"""

# Tupla com vários elementos
tupla1 = (1, 2, 3)

# Tupla com tipos mistos
tupla2 = ("a", 3.14, True)

# Tupla sem parênteses (Python infere)
tupla3 = 4, 5, 6

# Tupla com um único elemento (vírgula é obrigatória)
tupla4 = (10,)

# prints das tuplas
print(tupla1)
print(tupla2)
print(tupla3)
print(tupla4)

#------------

vendas = (
    "Antonio",        # Índice 0 - Nome
    "2020-05-10",     # Índice 1 - Data de contratação
    "1985-03-22",     # Índice 2 - Data de nascimento
    20000.00,         # Índice 3 - Salário
    "Vendedor"        # Índice 4 - Cargo
)

# Criando variáveis com base nos índices da tupla
nome = vendas[0]
data_contratacao = vendas[1]
data_nascimento = vendas[2]
salario = vendas[3]
cargo = vendas[4]

# ------

sales = (
    "Antonio",        # Índice 0 - Nome
    "2020-05-10",     # Índice 1 - Data de contratação
    "1985-03-22",     # Índice 2 - Data de nascimento
    20000.00,         # Índice 3 - Salário
    "Vendedor"        # Índice 4 - Cargo
)

# unpacking
name, date_hire, birth_date, salary, position = sales

print(name)
print(date_hire)
print(birth_date)
print(salary)
print(position)
