número = int(input('Digite um número e direi se é primo: '))
é_primo = True

for possível_divisor in range(2, número//2 + 1):
  print(f'Divisor: {possível_divisor}')
  if número % possível_divisor == 0:
    é_primo = False

print('é primo') if é_primo else print('não é primo')