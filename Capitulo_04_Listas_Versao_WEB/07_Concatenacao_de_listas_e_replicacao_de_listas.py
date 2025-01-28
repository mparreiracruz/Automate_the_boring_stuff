# Listas podem ser concatenadas e replicadas assim como strings.
# O operador + combina duas listas para criar um novo valor de
# lista e o operador * pode ser usado com uma lista e um valor
# inteiro para replicar a lista.

soma_listas = [1, 2, 3] + ['A', 'B', 'C']
print(soma_listas)

multiplicacao_listas = ['X', 'Y', 'Z'] * 3
print(multiplicacao_listas)

spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)
