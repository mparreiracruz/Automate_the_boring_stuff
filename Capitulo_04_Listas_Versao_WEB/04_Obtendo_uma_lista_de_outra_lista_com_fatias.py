# Assim como um índice pode obter um único valor de uma lista,
# uma fatia pode obter vários valores de uma lista, na forma de uma nova lista.
# Uma fatia é digitada entre colchetes, como um índice, mas tem dois inteiros
# separados por dois pontos. Observe a diferença entre índices e fatias.

spam = ['gato', 'morcego', 'rato', 'elefante']
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])
print(spam[:2])
print(spam[1:])
print(spam[:])