preco = float(input('Qual é o preço do produto? R$'))
novo = preco - (preco * 5 / 100)
print('O preço do produto é {}, com desconto de 5% o novo preco {}'.format(preco, novo))