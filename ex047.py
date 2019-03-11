nota = float(input('Nota (0/10): '))
notas = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

while nota not in notas:
    nota = float(input('Nota inválida, tente novamente. Nota (0/10): '))
print(f'Nota registrada com sucesso. NOTA: {nota}')
