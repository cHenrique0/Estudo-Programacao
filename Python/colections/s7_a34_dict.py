# Seção 7 - Colections
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
    # Obs: Em algumas linguagens, o dicionario Python é conhecido por mapa.
    #
    # Um dicionario é uma coleção do tipo chave/valor.
    # O dicionario é representado pelas chaves: {}.
    # Cada conjunto chave/valor é um elemento do dicionario.
    # Chave e valor são separados por : (dois pontos) > {chave: valor}.
    # Tanto a chave quanto o valor podem ser de quaisquer tipos de dados.

# Criando um dicionario:
    #
    # FORMA 1 - Usando {chave: valor}:
"""
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
"""
    # FORMA 2 - Usando a função dict(chave=valor):
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
    # OBS: Diferente das listas e tuplas, os dicionarios não são indexados,
    # ou seja, não possuem indices para os elementos.
    #
    # FORMA 1 - Acessando via "chaves" com a mesma sintaxe que as listas.
        # dicionario["chave"] -> Retorna o valor da chave indicada.
"""
print(paises["br"])
print(paises["py"])
"""

    # FORMA 2 - Acessando via .get("chave"):
        # Caso o get() não encontre a chave informada, o metedo retorna o valor None.
"""
print(paises.get("br"))
print(paises.get("eua"))
print(paises.get("py"))
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
        # dicionario["chave"] = valor
"""
receita['abr'] = 350
print(receita)
"""

    # FORMA 2:
        # 1. Criar um novo dicionario: novo_dict = {chave: valor}
        # 2. Usar o metodo update():
            # 2.1. dicionario.update(novo_dict)
            # 2.2. dicionario.update({chave: valor})
"""
novo_dado = {'mai': 500}
receita.update(novo_dado)
# receita.update({'mai': 500})
print(receita)
"""

# Atualizando dados em um dicionario:
    #
    # FORMA 1:
        # dicionario[chave] = novo_valor -> o valor atual será substituido pelo novo_valor
"""
receita['mai'] = 550
print(receita)
"""
    # FORMA 2:
        # dicionario.update({chave:valor})
"""
receita.update({'mai': 600})
print(receita)
"""

    # OBS 1: a forma de adicionar e atualizar novos dados num dicionario é a mesma.
    # OBS 2: os dicionarios NÃO podem ter chaves repetidas.

# Remover dados de um dicionario:
    #
    # FORMA 1:
        # dicionario.pop(chave) -> remove a chave correspondente.
        # É obrigatorio informar a chave a ser removida.
        # A função pop() remove a chave e retorna o valor dela.
"""
receita = {'jan': 100, 'fev': 120, 'mar': 300}
ret = receita.pop('mar')
print(ret)
print(receita)
"""
    # FORMA 2:
        # del dicionario[chave] - remove a chave correspondente
"""
del receita['fev']
print(receita)
"""



# Apagando os dados do dicionario
    #
    # dicionario.clear() -> limpa os dados do dicionario deixando-o vazio.

"""
d = dict(a=1, b=2, c=3)
d.clear()
print(d)
"""

# Copiando um dicionario
    #
    # FORMA 1 - Deep Copy:
        # dicionario.copy() -> copia o dicionario para uma nova variavel
"""
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
"""
dic = {"aaa": 10, "bbb": 20, "ccc": 30}

for chave in dic:   # Itreando sobra as chaves(keys)
    print(chave)

for valor in dic.values():  # Imprime os valores(values)
    print(valor)

for chave in dic:  # Imprime os valores(values)
    print(dic[chave])
"""
