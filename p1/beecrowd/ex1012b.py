# Ler três valores
a, b, c = str ( input ()).split()

# Amazenar os valores em variáveis simples
# com um dígito após o ponto decimal
a = round ( float (a), 2)
b = round ( float (b), 2)
c = round ( float (c), 2)

# Declarar variável
pi = 3.14159

# Amazenar área de triângulo que possuí 
# a por base e c por altura
triangulo = ( a * c ) / 2

# Armazenar área do circulo de raio c
circulo = pi * c ** 2

# Armazenar área de trapézio que possuí
# a e b por bases e c por ALtura
trapezio = (( a + b ) * c ) / 2

# Amazenar área de quadrado que tem lado b
quadrado = b ** 2

# Armazenar área de retângulo que tem lados a e b
retangulo = a * b

# Imprimir todos os valores de área na tela
print (f'''TRIANGULO: {triangulo:.3f}
CIRCULO: {circulo:.3f}
TRAPEZIO: {trapezio:.3f}
QUADRADO: {quadrado:.3f}
RETANGULO: {retangulo:.3f}''')
