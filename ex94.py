pessoas = {}
lista = []
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('NOME:')).strip().upper()
    while True:
        pessoas['Sexo'] = str(input('SEXO:')).strip().upper()
        if pessoas['Sexo'] in 'MF':
            break
        print(f'Vc digitou errado! Digite [M/F]:')
    pessoas['Idade'] = int(input('Idade:'))
    lista.append(pessoas.copy())
    while True:
        resp = str(input('Você que continuar: [S/N]')).strip().upper()
        if resp in 'SN':
            break
        print(f'Você digitou errado! [S/N]')
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo foram {len(lista)} cadastrados.')
soma = 0
for p in lista:
    soma += p['Idade']
media = soma / len(lista)
print(f'A média da idade é {media}')
print(f'As mulheres cadastradas são ', end='')
for p in lista:
    if p['Sexo'] in 'Ff':
     print(f'{p['Nome']}')
print()
print(f'Lista de pessoas acima da média ', end='')
for p in lista:
    if p['Idade'] >= media:
      print(f'  ',end='')
      for k, v in p.items():
          print(f'{k} = {v}; ', end='')
      print()
print('<<< ENCERRADO >>>')


