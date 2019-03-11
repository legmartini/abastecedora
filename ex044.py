print('1- GASOLINA')
print('2- ÁLCOOL')
comb = int(input('Tipo de combustível? '))
litro = int(input('Quantos litros de combustível? '))

precoGas = 2.50
precoAlc = 1.90

if comb == 1 and litro < 20:
    descGas1 = 2.50 * 0.04
    precoGas1 = precoGas - descGas1
    valor = precoGas1 * litro
    print(f'Você abasteceu {litro} litros de GASOLINA e o custo normal seria R${precoGas * litro}0')
    print('Pagando a vista fica R$%.2f' % valor)

if comb == 1 and litro >= 20:
    descGas2 = 2.50 * 0.06
    precoGas2 = precoGas - descGas2
    valor = precoGas2 * litro
    print(f'Você abasteceu {litro} litros de GASOLINA e o custo normal seria R${precoGas * litro}0')
    print('Pagando a vista fica R$%.2f' % valor)

if comb == 2 and litro < 20:
    descAlc1 = 1.90 * 0.03
    precoAlc1 = precoAlc - descAlc1
    valor = precoAlc1 * litro
    print(f'Você abasteceu {litro} litros de ÁLCOOL e o custo normal seria R${precoAlc * litro}0')
    print('Pagando a vista fica R$%.2f' % valor)

if comb == 2 and litro >= 20:
    descAlc2 = 1.90 * 0.05
    precoAlc2 = precoAlc - descAlc2
    valor = precoAlc2 * litro
    print(f'Você abasteceu {litro} litros de ÁLCOOL e o custo normal seria R${precoAlc * litro}0')
    print('Pagando a vista fica R$%.2f' % valor)

