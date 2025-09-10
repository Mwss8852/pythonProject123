numero = int(input('Digite um numero?'))
print(f"\n tabuada do numero {numero}:\n")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
