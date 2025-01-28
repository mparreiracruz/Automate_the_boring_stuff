# Quando você começa a escrever programas, é tentador criar
# muitas variáveis individuais para armazenar um grupo de valores similares.
# Acontece que essa é uma maneira ruim de escrever código.
# (Além disso, eu não tenho tantos gatos assim, juro.)
# Por um lado, se o número de gatos mudar, seu programa
# nunca será capaz de armazenar mais gatos do que você
# tem variáveis. Esses tipos de programas também têm muito
# código duplicado ou quase idêntico neles.


print('Digite o nome do gato 1:')
catName1 = input()
print('Digite o nome do gato 2:')
catName2 = input()
print('Digite o nome do gato 3:')
catName3 = input()
print('Digite o nome do gato 4:')
catName4 = input()
print('Digite o nome do gato 5:')
catName5 = input()
print('Digite o nome do gato 6:')
catName6 = input()
print('Os nomes dos gatos são:')
print(catName1 + ' ' + catName2 + ' ' + catName3 + ' ' + catName4 + ' ' +
catName5 + ' ' + catName6)