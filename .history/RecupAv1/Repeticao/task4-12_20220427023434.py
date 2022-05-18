quant = int(input('Quantos números serão digitados? '))

aux = 0
for cont in range(quant):
  aux = int(input('Digite um número: '))
  aux += aux

print(f'A média é: {aux/quant}')