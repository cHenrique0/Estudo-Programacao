#
# Modulo Collections
#
#
# NAMED TUPLE
#
# É uma tupla que recebe um nome e parametros.

from collections import namedtuple

# CRIANDO UMA NAMEDTUPLE:
    # Declaração do nome e dos parametros:
        #
        # FORMA 1:
        #
        # cachorro = namedtuple("Cachorro", "idade raca nome")
        #
        #
        # FORMA 2:
        #
        # cachorro = namedtuple("Cachorro", "idade, raca, nome")
        #
        #
        # FORMA 3:
        # USAR ESTA FORMA POIS É MELHOR DE VISUALIZAR OS PARAMETROS
        #

cachorro = namedtuple("Cachorro", ["idade", "raca", "nome"])

    # Usando a named tupla declarada:

zeus = cachorro(idade=9, raca="Cocker-Speniel", nome="Zeus")
print(zeus)

# Acessando os dados:
    #
    # FORMA 1:
        # Usando os indices como numa tupla convencional.
"""
print(zeus[0])
print(zeus[1])
print(zeus[2])
"""
    #
    # FORMA 2:
        # variavel.parametro -> informando o parametro que foi declarado.
"""
print(zeus.idade)
print(zeus.raca)
print(zeus.nome)
"""