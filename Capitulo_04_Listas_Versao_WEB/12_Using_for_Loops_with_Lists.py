# No Capítulo 2 , você aprendeu sobre o uso de loops
# for para executar um bloco de código um certo número
# de vezes. Tecnicamente, um loop for repete o bloco
# de código uma vez para cada item em um valor de lista.

for i in range(4):
    print(i)

for i in [0, 1, 2, 3]:
    print(i)

# O loop for anterior na verdade percorre sua cláusula com a
# variável i definida como um valor sucessivo na lista [0, 1, 2, 3] em cada iteração.
# Uma técnica comum do Python é usar range(len( someList ))
# com um loop for para iterar sobre os índices de uma lista.

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])