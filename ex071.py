eleitores = int(input('Quantos eleitores votarão? '))

print('''Candidato #1: 11
Candidato #2: 22
Candidato #3: 33''')

cand1 = 0
cand2 = 0
cand3 = 0
nulo = 0

for c in range(eleitores):
    votos = int(input(f'Voto #{c+1}: '))

    if votos == 11:
        cand1 += 1
    elif votos == 22:
        cand2 += 1
    elif votos == 33:
        cand3 += 1
    else:
        nulo += 1

if cand1 > cand2 and cand1 > cand3:
    print(f'Candidato #1 venceu com {cand1} votos.')
if cand2 > cand1 and cand2 > cand3:
    print(f'Candidato #1 venceu com {cand2} votos.')
if cand3 > cand1 and cand3 > cand1:
    print(f'Candidato #1 venceu com {cand3} votos.')

print(f'Candidato #1 recebeu {cand1} votos.')
print(f'Candidato #2 recebeu {cand2} votos.')
print(f'Candidato #3 recebeu {cand3} votos.')
print(f'{nulo} votos nulos.')



