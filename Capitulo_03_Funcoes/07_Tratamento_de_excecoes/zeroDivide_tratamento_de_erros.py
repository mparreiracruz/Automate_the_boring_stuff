def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Erro: Argumento inválido')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))