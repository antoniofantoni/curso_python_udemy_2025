# Strings são case-sensitive
# Strings são imutáveis (immutable)
# Strings são indexadas (0, 1, 2, 3, ...)     
# Strings são iteráveis (for, in, while, etc.)
# Strings são fatiáveis (slicing)   
# Strings são concatenáveis (+)
# Strings são multiplicáveis (*)    
# Strings são comparáveis (==, !=, <, >, <=, >=)
# Strings são formatáveis (f-strings, format(), %)    
# Strings são indexáveis ([], [:], [::])
# Strings são convertíveis (str(), int(), float(), bool(), list(), tuple(), dict(), set())
# Strings são codificáveis (encode(), decode()) 
# Strings são decodificáveis (decode()) 
nome = 'Lucas'
sobrenome = 'Lima'  
nome = "Antonio"  
print(nome)  # Antonio

# Strings com mais de uma linha
# \n quebra de linha
# \t tabulação  
# \r retorno de carro
# \b backspace    
#exemplo de string com aspas duplas triplas
line = "="
descricao = """Lucas Lima é um programador Python.
\tEle é muito bom em Python e Django.   
Ele também é bom em JavaScript e React.
Ele é um ótimo desenvolvedor full stack."""
print(line * 20)  # ====================
print(descricao) 
print("Ele" in descricao)  # True




