#
# Modulo Collections
#
#
# Collection > High-Performance Container Datetype
#
#
# COUNTER (contador):
    #
    # Recebe um iteravel como parametro e cria um objeto do tipo
    # Collections Counter, que é parecido com um dicionario, contendo como
    # chave o elemento do iteravel e como valor a quantidade de ocorrencia
    # desse elemento.

# Utilizando o Counter:
from collections import Counter

"""
print("EX1: Usando lista como parametro pro Counter")
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 44]
# não é necessário guardar o resultado numa variavel.
# guardei o resultado apenas para verificar qual o tipo gerado pelo Counter()
result = Counter(lista)
print(type(result))
print(result)

print("EX2: Usando string como parametro pro Counter")
print(Counter("Some String"))
"""

print("EX3:")
texto = """A Wikipédia é um projeto de enciclopédia colaborativa, universal e multilíngue
estabelecido na internet sob o princípio wiki. Tem como propósito fornecer um conteúdo 
livre, objetivo e verificável​​, que todos possam editar e melhorar. O projeto é definido 
pelos princípios fundadores. O conteúdo é disponibilizado sob a licença Creative Commons 
BY-SA e pode ser copiado e reutilizado sob a mesma licença — mesmo para fins comerciais — 
desde que respeitando os termos e condições de uso."""

palavras = texto.split()
result = Counter(palavras)
print(result)
print(result.most_common(5))    # 5 paralavras com mais ocorrência no texto

