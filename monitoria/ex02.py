valor = int ( input ())
print(valor)

notas100 = valor // 100
notas50 = valor % 100 // 50
notas20 = valor % 100 % 50 // 20
notas10 = valor % 100 % 50 % 20 // 10
notas5 = valor % 100 % 50 % 20 % 10 // 5
notas2 = valor % 100 % 50 %20  % 10 % 5 // 2
notas1 = valor % 100 % 50 % 20 % 10 % 5 % 2 // 1

print(f'{notas100} nota(s) de R$ 100,00')
print(notas50)
print(notas20)
print(notas10)
print(notas5)
print(notas2)
print(notas1)