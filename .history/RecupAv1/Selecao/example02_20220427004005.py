CASAS_DECIMAIS = 2
PRECISÃO = 10**-CASAS_DECIMAIS
x = float(input('x: '))
y = float(input('y: '))

print('Os números são iguais') if (abs(x-y) < PRECISÃO) else print('Os números são diferentes')