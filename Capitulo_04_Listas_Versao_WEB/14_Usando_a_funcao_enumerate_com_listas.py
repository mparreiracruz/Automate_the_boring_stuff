# Em vez de usar a técnica range(len( someList )) com um
# loop for para obter o índice inteiro dos itens na lista,
# você pode chamar a função enumerate() . Em cada iteração
# do loop, enumerate() retornará dois valores:
# o índice do item na lista e o item na lista em si.

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)