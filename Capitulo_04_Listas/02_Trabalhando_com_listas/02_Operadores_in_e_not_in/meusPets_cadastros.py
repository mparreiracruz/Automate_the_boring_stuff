meusPets = ['Otto', 'Bone', 'Jon']
print('Entre com o nome do seu pet: ')
nome = input()

if nome not in meusPets:
    print(f'Eu não tenho o nome {nome} nos meus dados.')
    print('Deseja cadastrar esse nome? (s/n)')
    resposta = input().lower()
    if resposta == 's':
        meusPets.append(nome)
        print(f'{nome} foi adicionado à lista de pets!')
    else:
        print('O nome não foi adicionado.')
else:
    print(f'Encontrei o(a) {nome}!')

print('Lista atualizada de pets:', meusPets)