#A instrução del excluirá valores em um índice em uma lista.
# Todos os valores na lista após o valor excluído serão movidos
# um índice acima.

spam = ['gato', 'morcego', 'rato', 'elefante']
del spam[2]
print(spam)

del spam[2]
print(spam)

# A instrução del também pode ser usada em uma variável simples para excluí-la,
# como se fosse uma instrução “unassignment”. Se você tentar usar a variável
# após excluí-la, receberá um erro NameError porque a variável não existe mais.
# Na prática, você quase nunca precisa excluir variáveis ​​simples.
# A instrução del é usada principalmente para excluir valores de listas.