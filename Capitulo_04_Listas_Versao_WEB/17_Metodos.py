# Um método é a mesma coisa que uma função, exceto que é “chamado em” um valor.
# Por exemplo, se um valor de lista fosse armazenado em spam , você chamaria o
# método de lista index() (que explicarei em breve) nessa lista assim: spam.index('hello').
# A parte do método vem depois do valor, separada por um ponto.
# Cada tipo de dado tem seu próprio conjunto de métodos. O tipo de dado list, por exemplo,
# tem vários métodos úteis para encontrar, adicionar, remover e manipular valores em uma lista.
# Os valores de lista têm um método index() que pode receber um valor,
# e se esse valor existir na lista, o índice do valor será retornado.
# Se o valor não estiver na lista, o Python produzirá um erro ValueError.

spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))
print(spam.index('heyas'))
print(spam.index('howdy howdy howdy'))

# Quando há duplicatas do valor na lista, o índice de sua primeira aparição é retornado.
# Insira o seguinte no shell interativo e observe que index() retorna 1 , não 3.

spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print(spam.index('Pooka'))

