print('Iniciando nova venda...')
total = 0

while True:
  preço = int(input('Digite o preço do produto:'))
  if not preço:
    break
  total += preço

print('Total da venda:', total)