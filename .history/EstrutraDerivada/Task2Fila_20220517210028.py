fila = []
while True:
  comando = print("Digite 'c' para chegada e 'a' para atender: ")

  if comando == 'c':
    nome = input("Digite o nome do paciente: ")
    fila.append(nome)
  elif comando == 'a':
    nome = fila.pop(0)
    print(nome)