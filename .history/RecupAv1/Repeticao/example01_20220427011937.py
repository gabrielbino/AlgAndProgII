PROMPT = 'Digite o preço do produto:'

print('Iniciando nova venda...')

total = 0
preço = int(input(PROMPT))

while preço != 0:
  total += preço
  preço = int(input(PROMPT))

print('Total da venda:', total)