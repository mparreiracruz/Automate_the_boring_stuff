spam = ['maçãs', 'bananas', 'tofus', 'gatos']

def remover_s(spam):
    return [item[:-1] if item.endswith('s') else item for item in spam]
      return ', '.join(lista[:-1]) + ', and ' + lista[-1]
resultado = remover_s(spam)

print(resultado)