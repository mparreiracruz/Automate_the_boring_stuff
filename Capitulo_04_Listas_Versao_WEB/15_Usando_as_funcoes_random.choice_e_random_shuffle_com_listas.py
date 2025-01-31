# O módulo random tem algumas funções que aceitam listas para argumentos.
# A função random.choice() retornará um item selecionado aleatoriamente da lista.

import random

animais  = ['Cachorro', 'Gato', 'Morça']

print(random.choices(animais))
print(random.choices(animais))
print(random.choices(animais))

# Você pode considerar random.choice(someList) como uma forma mais
# curta de someList[random.randint(0, len(someList) – 1] .
# A função random.shuffle() reordenará os itens em uma lista.
# Esta função modifica a lista no lugar, em vez de retornar uma nova lista.

pessoas = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(pessoas)
print(pessoas)
random.shuffle(pessoas)
print(pessoas)

