# formas de importar um modulo
# 1. importando o modulo inteiro exemplo: import math_operations
# 2. importando funções específicas do modulo
# 3. importando o modulo com um alias

from math_operations import soma, subtrai
import math_operations 
import math_operations as op

import strings_utils as s_utils
from strings_utils import capitalize_string as cs, contar as c, uppercase as u



print(cs("olá mundo"))# usando importação direta de função
# Testando o modulo de strings

print(soma(5, 3))# usando importação direta
print(math_operations.soma(5, 3))# usando importação inteira do modulo
print(op.soma(5, 3))# usando importação por alias

print(f"{op.divide(5,3):.2f}")# usando importação por alias e formatando a saída

print(cs("antonio"))# usando importação direta de função
print(c("Antonio"))# usando importação direta de função
print(u("antonio"))# usando importação direta de função





