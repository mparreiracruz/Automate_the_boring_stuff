try:
    spam = [1, 3, 2, 4, 'Alice', 'Bob']
    spam.sort()
    print(spam)

except TypeError:
    print('Erro: tipos de variáveis incompatíveis.')