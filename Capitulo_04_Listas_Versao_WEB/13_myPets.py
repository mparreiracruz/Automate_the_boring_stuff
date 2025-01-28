# Você pode determinar se um valor está ou não em uma
# lista com os operadores in e not in . Como outros operadores,
# in e not in são usados ​​em expressões e conectam dois
# valores: um valor a ser procurado em uma lista e a lista onde
# ele pode estarencontrado.
# Por exemplo, o programa a seguir permite que o usuário digite
# o nome de um animal de estimação e, em seguida, verifica se o
# nome está em uma lista de animais de estimação.

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Digite o nome de um animal de estimação:')
name = input()
if name not in myPets:
    print('Eu não tenho um animal de estimação chamado ' + name)
else:
    print(name + ' é meu animal de estimação.')
