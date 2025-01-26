print('Olá, mundo!')
print('Qual é seu nome?')

meu_Nome = input()

print('Olá ' + meu_Nome + '!')
print('Seu nome tem {} caracteres.'.format(len(meu_Nome)))

print('Qual é a sua idade?')
minha_Idade = input()

# Convertendo a entrada para float e arredondando
idade_arredondada = round(float(minha_Idade))

# Calculando a idade no próximo ano
print('Você fará ' + str(idade_arredondada + 1) + ' anos em um ano.')
