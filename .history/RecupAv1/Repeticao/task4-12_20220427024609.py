quant = int(input('Quantos números serão digitados? '))

aux = 0
for cont in range(quant):
  valor = int(input('Digite um número: '))
  aux += valor

print(f'A média é: {valor / (quant-1)}')