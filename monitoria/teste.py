def fatorial(num):
  if num < 2:
    return 1
  return num * fatorial(num - 1)

# 5! = 5 * 4 * 3 * 2 * 1
print(fatorial(5))

# fat(5) -> 5 * fat(5 - 1)
# fat(4) -> 4 * fat(4 - 1)
# fat(3) -> 3 * fat(3 - 1)
# fat(2) -> 2 * fat(2 - 1)
# fat(1) -> 1

def potencia(base, exp):
  if exp == 0:
    return 1
  return base * potencia(base, exp - 1)

# 2**3 = 2 * 2 * 2
print(potencia(2, 3))

# pot(2, 3) -> 2 * pot(2, 2)
# pot(2, 2) -> 2 * pot(2, 1)
# pot(2, 1) -> 2 * pot(2, 0)
# pot(2, 0) -> 1

def somaInteiros(num):
  if num > 0:
    return num + somaInteiros(num - 1)
  if num < 0:
    return num + somaInteiros(num + 1)
  return num

# 15 = 1 + 2 + 3 + 4 + 5
print(somaInteiros(-5))

# soma(5) -> 5 + soma(4)
# soma(4) -> 4 + soma(3)
# soma(3) -> 3 + soma(2)
# soma(2) -> 2 + soma(1)
# soma(1) -> 1 + soma(0)
# soma(0) -> 0

def contaInteiros(num, busca, contador = 0):
  if num > 0:
    ultimoAlgarismo = num % 10
    if ultimoAlgarismo == busca:
      contador += 1
    num //= 10
    return contaInteiros(num, busca, contador)
  return contador


def contaInteirosComWhile(num, busca):
  contador = 0
  while num > 0:
    ultimoAlgarismo = num % 10
    if ultimoAlgarismo == busca:
      contador += 1
    num //= 10
  return contador



print(contaInteirosComWhile(122342, 2))

# cont(122342, 2) -> ult = 2 se 2 == busca, cont += 1, num = 12234 -> cont(12234, 2, 1)
# cont(12234, 2, 1) -> ult = 4 se 2 == busca, num = 1223 -> cont(1223, 2, 1)
# cont(1223, 2, 1) -> ult = 3 se 2 == busca, num = 122 -> cont(122, 2, 1)
# cont(122, 2, 1) -> ult = 2 se 2 == busca, cont += 1, num = 12 -> cont(12, 2, 2)
# cont(12, 2, 2) -> ult = 2 se 2 == busca, cont += 1, num = 1 -> cont(1, 2, 3)
# cont(1, 2, 3) -> ult = 1 se 2 == busca, num = 0 -> cont(0, 2, 3)
# cont(1, 2, 3) -> 3

def ehNumeroPrimero(num):
  contador = 0
  for i in range(1, num + 1):
    if num % i == 0:
      contador += 1
  return contador == 2


def primosAteNum(num):
  contadorPrimos = 0
  for i in range(1, num + 1):
    if ehNumeroPrimero(i):
      contadorPrimos += 1
  return contadorPrimos


print(primosAteNum(10))
print(ehNumeroPrimero(5))
# primo(5) ->
# cont = 0, i = 1, se 6 % 1 == 0, cont += 1
# cont = 1, i = 2, se 6 % 2 == 0, cont += 1
# cont = 2, i = 3, se 6 % 3 == 0, cont += 1
# cont = 3, i = 4, se 6 % 4 == 0
# cont = 3, i = 5, se 6 % 5 == 0
# cont = 3, i = 6, se 6 % 6 == 0, cont += 1
# return 4 == 2 -> true