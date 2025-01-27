# Os elementos de uma lista em Python são
# acessados por índices, começando em 0,
# com o último índice sendo um a menos que o tamanho da lista.

spam = ['gato', 'morcego', 'rato', 'elefante']
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])

spam = ['gato', 'morcego', 'rato', 'elefante'][3]
print(spam)

spam = ['gato', 'morcego', 'rato', 'elefante']
print('Olá, ' + spam[0])

print('O ' + spam[1] + ' comeu o ' + spam[0] + '.')

spam = ['gato', 'morcego', 'rato', 'elefante']
#print(spam[10000])# Código com erro proposital

spam = ['gato', 'morcego', 'rato', 'elefante']
print(spam[1])
#print(spam[1.0])# Código com erro proposital
print(spam[int(1.0)])

#Listas também podem conter outros valores de lista.
# Os valores nessas listas de listas podem ser
# acessados usando múltiplos índices, como:

spam = [['gato', 'morcego'], [10, 20, 30, 40, 50]]
print(spam[0])
print(spam[0][1])
print(spam[1][4])

