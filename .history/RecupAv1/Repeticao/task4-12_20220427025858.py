quant = int(input('Quantos números serão digitados? '))

aux = 0
for cont in range(quant + 1):
  number = int(input('Digite um número: '))
  aux += number

print(f'A média é: {aux/quant}')