meusPets = ['Otto', 'Bone', 'Jon']
print('Entre com o nome do seu pet: ')
nome = input()

if nome not in meusPets:
    print('Eu não tenho o nome ' + nome + ' nos meus dados.' )
else:
    print('encontrei o(a) ' + nome)    