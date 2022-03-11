#
# Modulo Collections
#
#
# DEQUE
#
# Pode-se dizer que um deque é uma lista de alta performance.
# O deque possui os mesmos metodos da lista e alguns metodos extras.

from collections import deque

deq = deque("Geek")
print(deq)

# Adicionando elementos ao deque:

deq.append('y') # Adiciona o elemento ao fim do deque
print(deq)

deq.appendleft('k') # Adiciona no começo do deque
print(deq)

# Removendo elementos do deque:

print(deq.pop()) # Remove e retornao ultimo elemento do deque
print(deq)

print(deq.popleft()) # Remove e retorna o primeiro elemento do deque
print(deq)