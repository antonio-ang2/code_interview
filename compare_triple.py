alice = [1, 2, 3]
bob = [3, 2, 1]


def compareTriplets(a, b):
    pa = 0
    pb = 0
    for z in range(len(b)):
        if a[z] > b[z]:
            pa += 1
        elif b[z] > a[z]: 
            pb += 1
        else:
            pass
    if pa > pb:
        champ = 'pa'
    elif pb > pa:
        champ = 'pb'
    else:
        champ = 'empate'
    print(f'E o campeão foi {champ}') if pa != pb else print('deu empate')
    return champ
    # loop encadeado, o que eu preciso: percorrer a lista de dentro comparando valores com a da fora.

compareTriplets(alice, bob)