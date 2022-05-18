def mmc(x, y):
  candidato = max(x, y)
  while not(candidato % x == 0 and candidato % y == 0):
    candidato += 1
    return candidato

assert mmc(12, 10) == 60
assert mmc(3, 9) == 9
assert mmc(14, 15) == 210

print('Todos os testes finalizados com sucesso!')