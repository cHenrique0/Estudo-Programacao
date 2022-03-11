#
#
# Documentando funções com Docstrings:
    #
    # Docstring é uma explicação do que a função faz
    # Podemos ter acesso a documentação de uma função utilizando a propriedade __doc__
    #
#
#


def diz_oi():
    """
'diz_oi'.

    Uma função simples que retorna a string 'Oi'.
    """
    return "Oi"

# print(diz_oi.__doc__)   # Imprime a docstring da função diz_oi()


def potencia(num, pot=2):
    """Função que retorna, por padrão, o quadrado de 'num' ou 'num' elevado à 'pot' informada

    Args:
        num (int): número base da exponenciação
        pot (int, optional): número que será a potencia. Defaults to 2.

    Returns:
        int: resultado da exponenciação.
    """
    return num ** pot

