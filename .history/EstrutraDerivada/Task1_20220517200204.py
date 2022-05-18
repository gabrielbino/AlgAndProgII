from random import shuffle

# Gabriel Fernandes Bino - Algoritmos e Programação II
baralho = jogadores = []

# for i in range(4):
#   for carta in range(1, 14):
#     baralho.append(carta)
#     shuffle(baralho)
# print(baralho)

def distribuir(baralho):
  jogadores = ([], [])
  jogador = 0
  
  while len(baralho) > 0:
    carta = baralho.pop()
    
    jogadores[jogador].append(carta)
    
    jogador += 1
    jogador %= 2 # 2 representa a quantidade de jogadores

    if jogador == 0:
      jogador = 1
    else:
      jogador = 0

  return jogadores

cartasGanhas = ([], [])
mesa = []

assert len(jogadores[0]) == len(jogadores[1])

while len(jogadores[0]) > 0:
  mesa.append(jogadores[0].pop())
  mesa.append(jogadores[1].pop())

  if mesa[-1] > mesa[-2]:
    ganhador = 1
  elif mesa[-1] < mesa[-2]:
    ganhador = 0
  else:
    ganhador = None
  
  print(f"Mesa: {mesa} Ganhador: {ganhador}")

while ganhador != None and len(mesa) > 0:
  cartasGanhas[ganhador].append(mesa.pop())
print(cartasGanhas)

while len(mesa) > 0:
  cartasGanhas[ganhador].append(mesa.pop())

  if len(cartasGanhas[0]) > len(cartasGanhas[1]):
    print("Jogador 0 venceu!")
  elif len(cartasGanhas[0]) < len(cartasGanhas[1]):
    print("Jogador 1 venceu!")
  else:
    print("EMPATE!")
  
  print(f"{len(cartasGanhas[0])} x {len(cartasGanhas[1])}")
