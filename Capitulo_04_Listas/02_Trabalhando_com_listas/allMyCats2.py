nomeGatos = []
while True:
    print('Entre com o nome do gato ' + str(len(nomeGatos) + 1) + ' (ou digite nada para parar o programa): ')
    nome = input()
    if nome == '':
        break
    nomeGatos = nomeGatos + [nome]    
print('O nome dos gatos são: ')
for nome in nomeGatos:
    print('   ' + nome)    