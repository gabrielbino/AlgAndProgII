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

  elif comando == 'p':
    if not fila:
      break
    else:
      print("A fila ainda contém os seguintes nomes: ")
      
      for nome in fila:
        print(nome)
      
      opcao = input("Deseja parar mesmo assim? [S/N]").toUpper()
      
      if opcao == 'S':
        break
  else:
    print("Comando desconhecido.")
