def ler_int(mensagem, mensagem_de_erro):
  while True:
    try:
      entrada = int(input(mensagem))
      return entrada
    except ValueError:
      print(mensagem_de_erro)