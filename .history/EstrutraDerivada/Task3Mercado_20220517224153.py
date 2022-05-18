from random import random, randint

tempoSimulacao = 1000
chanceDeTerCliente = .05
maxProdutos = 100
numeroCaixas = 1

while True:
  tempoEspera = []
  tempoOciosidade = []
  filas = []

  for i in range(numeroCaixas):
    filas.append([])
    tempoOciosidade.append(0)

  for instante in range(tempoSimulacao):
    if random() < chanceDeTerCliente:
      cliente = [randint(1, maxProdutos), 0]

    menorFila = filas[0]
    
    for fila in filas:
      if len(fila) < len(menorFila):
        menorFila = fila
    menorFila.append(cliente)

    if fila:
      fila[0][0] -= 1 # Registra um produto do primeiro cliente

      for i in range(1, len(fila)):
        fila[i][1] += 1 # Incrementa tempo de espera dos demais
  
  assert numeroCaixas != 0 and tempoSimulacao != 0
  
  ociosidadeMedia = round(sum(tempoOciosidade)/numeroCaixas/tempoSimulacao, 2)

  if len(tempoEspera) != 0:
    esperaMedia = round(sum(tempoEspera)/len(tempoEspera))
  else:
    esperaMedia = 0
  
  print(f"Quantidade de caixas: {numeroCaixas}")
  print(f"Ociosidade média: {ociosidadeMedia}")
  print(f"Espera média: {esperaMedia}")
  print()

  if not input("Mais uma simulação? [S/N]: ") == 's':
    break
  numeroCaixas += 1