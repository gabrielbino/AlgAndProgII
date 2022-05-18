fila = []

while True:
  comando = input("Digite 'c' para chegada e 'a' para atender: ")

  if comando == 'c':
    nome = input("Digite o nome do paciente: ")
    fila.append(nome)
  elif comando == 'a':
    if fila:
      nome = fila.pop(0)
      print(nome)
    else:
      print("Não há ninguém na fila.")