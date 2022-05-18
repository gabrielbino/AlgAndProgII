from random import shuffle


baralho = []

for i in range(4):
  for carta in range(1, 14):
    baralho.append(carta)
    shuffle(baralho)
print(baralho)