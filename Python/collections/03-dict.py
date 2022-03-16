# Collections
#
# O python possui alguns tipos de coleções:
# i.    Listas
# ii.   Tuplas
# iii.  DICIONARIOS
# iv.   Mapas
# v.    Conjuntos
#
# 3. Dicionarios (dict):
    #
    # Um dicionario é uma coleção do tipo chave-valor.
    # O dicionario é representado pelas chaves: {}.
    # Cada conjunto chave-valor é um elemento do dicionario.
    # Chave e valor são separados por : (dois pontos) -> {chave: valor}.
    # Tanto a chave quanto o valor podem ser de quaisquer tipos de dados.
    # Um par chave-valor é um conjunto de valores associados um ao outro.
    # Obs: Em algumas linguagens, o dicionario Python é conhecido por mapa.

# Criando um dicionario:
    #
    # FORMA 1 - Usando {key: value}:
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
"""
print(paises)
"""
    # FORMA 2 - Usando a função dict(key=value):
"""
paises = dict(br="Brasil", eua="Estados Unidos", py="Paraguai")
print(paises)
"""
    # Outra forma de criar um dicionario:
"""
outro = {}.fromkeys('a', 'b')  # Os parametros são: 'a' - chave, 'b' - valor
print(outro)
"""

    # Podemos informar um objeto iteravel(lista, tuplas, strings) e um valor.
    # Para cada elemento nesse objeto, o dicionario associará o valor;
"""
usuario = {}.fromkeys(["nome", "pontos", "e-mail", "profile"], "desconhecido")
print(usuario)

teste = {}.fromkeys("SIM", 1) # Para cara letra na string, a função definirá como chave
print(teste)                  # e seu valor será 1.

"""
    # Podemos utilizar a função range()
"""
outro = {}.fromkeys(range(1, 11), "novo")
print(outro)
"""

# Acessando elementos:
    #
    # Diferente das listas e tuplas, os dicionarios não são indexados,
    # ou seja, não possuem indices para os elementos.
    #
    # FORMA 1 - Acessando via "chaves" com a mesma sintaxe que as listas.
        # dict[key] -> Retorna o valor da chave indicada.
"""
print(paises["br"])
print(paises["py"])
"""

    # FORMA 2 - Acessando via .get(key):
        # Caso o get() não encontre a chave informada, o metedo retorna o valor None.
"""
print(paises.get("br"))
print(paises.get("eua"))
print(paises.get("py"))
print(paises.get("uk"))
"""

    # Podemos passar um segundo parametro no get().
    # Caso o dicionario contenha a chave informada, o metodo retorna o valor,
    # se o dicionario NÃO contém a chave informada, o metodo retorna o segundo parametro informado.
"""
pais1 = paises.get('ru', "País não encontrado") # O dicionario paises nao tem a chave 'ru'
print(f"{pais1}")
pais2 = paises.get('py', "País não encontrado")
print(f"{pais2}")
"""

# Verificando se um dicionario contém uma CHAVE:
    # Retorna True se achar a chave ou False se não achar a chave.
"""
print('br' in paises)
print('ru' in paises)
print("Estados Unidos" in paises)
"""

# Adicionar elementos num dicionario
"""
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
"""
    # FORMA 1:
        # dict[key] = value
"""
receita['abr'] = 350
print(receita)
"""

    # FORMA 2:
        # 1. Criar um novo dicionario: new_dict = {key: value}
        # 2. Usar o metodo update():
            # 2.1. dicionario.update(new_dict)
            # 2.2. dicionario.update({key: value})
"""
novo_dado = {'mai': 500}
receita.update(novo_dado)
# receita.update({'mai': 500})
print(receita)
"""

# Atualizando dados em um dicionario:
    #
    # FORMA 1:
        # dict[key] = new_value -> o valor atual será substituido por new_value
"""
receita['mar'] = 550
print(receita)
"""
    # FORMA 2:
        # dict.update({key:value})
"""
receita.update({'mar': 600})
print(receita)
"""

    # OBS 1: a forma de adicionar e atualizar novos dados num dicionario é a mesma.
    # OBS 2: os dicionarios NÃO podem ter chaves repetidas.

# Remover dados de um dicionario:
    #
    # FORMA 1:
        # dict.pop(key) -> remove a chave correspondente.
        # É obrigatório informar a chave a ser removida.
        # A função pop() remove a chave e retorna o valor dela.
"""
receita = {'jan': 100, 'fev': 120, 'mar': 300}
ret = receita.pop('mar')
print(ret)
print(receita)
"""
    # FORMA 2:
        # del dict[key] - remove a chave correspondente
"""
del receita['fev']
print(receita)
"""



# Apagando os dados do dicionario
    #
    # dict.clear() -> limpa os dados do dicionario deixando-o vazio.

"""
d = dict(a=1, b=2, c=3)
print(d)
d.clear()
print(d)
"""

# Copiando um dicionario
    #
    # FORMA 1 - Deep Copy:
        # dict.copy() -> copia o dicionario para uma nova variavel
"""
d = dict(a=1, b=2, c=3)
print(d)
novo = d.copy()
print(novo)
novo['d'] = 4
print(d)
print(novo)
"""

    # FORMA 2 - Shallow Copy:
"""
novo = d
print(novo)
novo['d'] = 4
print(d)
print(novo)
"""

# Iterando sobre dicionarios:
dic = {"aaa": 10, "bbb": 20, "ccc": 30}
print(dic)

"""
for key in dic.keys():   # Iterando sobre as chaves(keys)
    print(key)

for key in dic: # tem o mesmo efeito do trecho acima
    print(key)

for value in dic.values():  # Imprime os valores(values)
    print(value)

for key in dic:  # Imprime os valores(values)
    print(dic[key])

for key, value in dic.items():  # itera sobre keys e values
    print(f"{key}: {value}")
"""