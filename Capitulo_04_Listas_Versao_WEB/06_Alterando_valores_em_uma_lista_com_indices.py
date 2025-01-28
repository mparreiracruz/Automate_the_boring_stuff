# Normalmente, um nome de variável vai no lado esquerdo de uma
# declaração de atribuição, como spam = 42 .
# No entanto, você também pode usar um índice de uma lista para alterar
# o valor naquele índice. Por exemplo, spam[1] = 'aardvark' significa
# “Atribuir o valor no índice 1 na lista spam à string 'aardvark' .”

spam = ['gato', 'morcego', 'rato', 'elefante']
spam[1] = 'porco-formigueiro'
print(spam)

spam[2] = spam[1]
print(spam)

spam[-1] = 12345
print(spam)