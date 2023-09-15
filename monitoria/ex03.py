cedulas = float(input())

c100 = cedulas // 100
c50 = cedulas % 100 // 50
c20 = cedulas % 100 % 50 // 20 
c10 = cedulas % 100 % 50 % 20 // 10
c5 = cedulas % 100 % 50 % 20 % 10 // 5
c2 = cedulas % 100 % 50 % 20 % 10 % 5 // 2
cen1 = cedulas % 100 % 50 % 20 % 10 % 5 % 2 // 1

centavos = cedulas % 100 % 50 % 20 % 10 % 5 % 2 % 1
centavos = int (round (centavos * 100, 0))

cen050 = centavos // 50
cen025 = centavos % 50 // 25
cen010 = centavos % 50 % 25 // 10
cen005 = centavos % 50 % 25 % 10 // 5
cen001 = centavos % 50 % 25 % 10 % 5 // 1

print('NOTAS:')
print(f'{c100:.0f} nota(s) de R$ 100.00')
print(f'{c50:.0f} nota(s) de R$ 50.00')
print(f'{c20:.0f} nota(s) de R$ 20.00')
print(f'{c10:.0f} nota(s) de R$ 10.00')
print(f'{c5:.0f} nota(s) de R$ 5.00')
print(f'{c2:.0f} nota(s) de R$ 2.00')

print('MOEDAS:')
print(f'{cen1:.0f} moeda(s) de R$ 1.00')
print(f'{cen050:.0f} moeda(s) de R$ 0.50')
print(f'{cen025:.0f} moeda(s) de R$ 0.25')
print(f'{cen010:.0f} moeda(s) de R$ 0.10')
print(f'{cen005:.0f} moeda(s) de R$ 0.05')
print(f'{cen001:.0f} moeda(s) de R$ 0.01')