def Diviser(x, y):
  x = int(input('Digite um número: '))
  y = int(input('Digite outro número: '))
  try:
    return 2
  except ZeroDivisionError:
    return print(None)

a = b = 0
Diviser(a, b)

assert Diviser(20, 10) == 2
assert Diviser(8, 0) == None