catNames = []
while True:
    print('Digite o nome do gato ' + str(len(catNames) + 1) +' (Ou não digite nada para parar.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # concatenação de lista
print('Os nomes dos gatos são:')
for name in catNames:
    print(' ' + name)
