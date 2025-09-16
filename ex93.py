jogador = {}
partidas = []

jogador['nome'] = str(input('Nome do jogador:'))
tot = int(input(f'Quantas partidas {jogador['nome']} jogou?'))

for c in range(tot):
    gols = int(input(f' Quantos gols na partida {c}?'))
    partidas.append(gols)

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)

print(f'O jogador {jogador['nome']} jogou {tot} partidas.')

for i, g in enumerate(jogador['gols']):
    print(f'   => Na partida {i}, fez {g} gols.')
print(f'Foi unm total de {jogador['total']} gols.')
