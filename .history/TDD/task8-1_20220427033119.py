def Diviser(x, y):
  x = int(input('Digite um número: '))
  y = int(input('Digite outro número: '))
  try:
    x/y
  except ZeroDivisionError:
    print(None)