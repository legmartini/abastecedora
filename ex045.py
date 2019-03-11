morango = float(input('KG de Morango: '))
maca = float(input('KG de Maça: '))

kilos = morango + maca

if morango <= 5.0:
    precoMor = 2.50
    valorTotal = precoMor * morango
    print(f'Você comprou {morango} kg de morango')
    print(f'O valor da compra é de {valorTotal}')
else:
    precoMor = 2.20
    valorTotal = precoMor * morango
    print(f'Você comprou {morango} kg de morango')
    print(f'O valor da compra é de {valorTotal}')

if maca <= 5.0:
    precoMac = 1.80
    valorTotal = precoMac * maca
    print(f'Você comprou {maca} kg de maça.')
    print(f'O valor da compra é de {valorTotal}')
else:
    precoMac = 1.50
    valorTotal = precoMac * maca
    print(f'Você comprou {maca} kg de maça.')
    print(f'O valor da compra é de {valorTotal}')

if kilos > 8.0 or valorTotal > 25.0:
    descTotal = valorTotal * 0.10
    valorTotal = descTotal - valorTotal
