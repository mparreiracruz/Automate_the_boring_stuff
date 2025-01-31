# Ao atribuir um valor a uma variável, você frequentemente
# usará a própria variável. Por exemplo, após atribuir 42
# à variável spam , você aumentaria o valor em spam em 1.

spam = 42
spam = spam + 1
print(spam)

# Como atalho, você pode usar o operador de atribuição
# aumentada += para fazer a mesma coisa:

spam = 42
spam += 1
print(spam)

# O operador += também pode fazer concatenação
# de strings e listas, e o operador *= pode fazer
# replicação de strings e listas.

spam = 'Olá, '
spam += ' mundo!'
print(spam)

bacon = ['Zophie']
bacon *= 3
print(bacon)
