"""
Exemplo 1: Arredondar um número decimal
"""
numero = 3.14159
resultado = round(numero, 2)  # Arredonda para 2 casas decimais
print(resultado)  # Saída: 3.14


"""
Exemplo 2: Arredondar para o inteiro mais próximo
"""
numero = 4.7
resultado = round(numero)  # Sem ndigits, arredonda para inteiro
print(resultado)  # Saída: 5


"""
Exemplo 3: Arredondar um número negativo
"""
numero = -5.678
resultado = round(numero, 1)  # Arredonda para 1 casa decimal
print(resultado)  # Saída: -5.7


"""
Exemplo 1: Valor absoluto de um número negativo
"""
numero = -10
resultado = abs(numero)
print(resultado)  # Saída: 10


"""
Exemplo 2: Valor absoluto de um número decimal
"""
numero = -3.14
resultado = abs(numero)
print(resultado)  # Saída: 3.14


"""
Exemplo 3: Uso em cálculos matemáticos
"""
x = -7
y = 3
diferenca = abs(x - y)  # Diferença absoluta entre dois números
print(diferenca)  # Saída: 10