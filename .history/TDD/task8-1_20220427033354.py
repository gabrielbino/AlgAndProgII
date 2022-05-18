def Diviser(x, y):
  x = int(input('Digite um número: '))
  y = int(input('Digite outro número: '))
  try:
    return x/y
  except ZeroDivisionError:
    return print(None)


a = b = 0
Diviser(a, b)