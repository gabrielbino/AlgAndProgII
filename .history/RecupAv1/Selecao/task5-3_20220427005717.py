from os import system


qualidade = int(input('Digite uma nota de 0 a 10: '))
if qualidade < 0 or qualidade > 10:
  print('Nota inválida.')
  system.exit(0)

preco = int(input('Digite uma nota de 0 a 10: '))
if preco < 0 or preco > 10:
  print('Nota inválida.')
  system.exit(0)

prazo = int(input('Digite uma nota de 0 a 10: '))
if prazo < 0 or prazo > 10:
  print('Nota inválida.')
  system.exit(0)