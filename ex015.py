k = float(input('Qual foi a quantidade de KM percorrido?'))
d = int(input('Qual foi a quantidade de DIAS alugado?'))
n = k * 0.15 + d * 60
print('O KM percorrido foi {} KM, a quantidade de dias foi {} Dias, total a ser pago R${:.2f}'.format(k, d, n,))
