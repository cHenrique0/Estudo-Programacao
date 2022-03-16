#
# Modulo Collections
#
#
# 1. DEFAULT DICT:
    #
    # Ao criar um dicionario utilizando o Default Dict, informamos um valor default,
    # podendo utilizar um lambda para isso.
    # Esse valor será utilizado sempre que não houver um valor definido na criação.
    # Caso tente-se acessar uma chave que não existe, essa chave será criada e o valor
    # default será atribuído.
    #
    # OBS: Lambdas são funções sem nome, que podem ou não receber parametros de entrada
    # e retornar valores.

from collections import defaultdict     # Importando o Default
from collections import OrderedDict     # Importando o Ordered Dict

"""
dic = defaultdict(lambda : 0)
dic["curso"] = "Programação em Python: Essencial"
print(dic)
print(dic["outro"])
print(dic)
"""
#
# 2. ORDERED DICT:
    #
    # É como um dicionário comum, porém, ele garante a ordem de inserção dos elementos.
"""

dic = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
for chave, valor in dic.items():
    print(f"{chave}: {valor}")
"""
#
# Diferença entre Dict e Ordered Dict:
#
"""
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)   # True > pois para o Dict a ordem de inserção não importa e não é garantida.

order1 = OrderedDict({'a': 1, 'b': 2})
order2 = OrderedDict({'b': 2, 'a': 1})
print(order1 == order2) # False > pois o Ordered Dict garante a ordem de inserção.
"""
