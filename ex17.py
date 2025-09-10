import math
numero = float(input('Digite o tamanho do cateto oposto?'))
numeros = float(input('Digite o comprimento do cateto adjacente?'))
total = math.sqrt(numero ** 2 + numeros ** 2)
print(f'O tamanho da hipotenusa é {total}')