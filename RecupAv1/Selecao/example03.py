print('Digite as três notas')
n1 = int(input('N1:'))
n2 = int(input('N2:'))
n3 = int(input('N3:'))

média = (n1+n2+n3)/3

if n3 >= 8:
  média += 1
if média > 10:
  média = 10
print('Média:', média)