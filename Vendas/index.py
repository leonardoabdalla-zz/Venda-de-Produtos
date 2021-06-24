produto = float(input('Qual o valor do produto? R$ '))
print(' 1 - à vista no dinheiro\n 2 - À vista no cartão\n 3 - Em té (2x) no cartão\n 4 - (3x) ou mis no cartão')
formaDePagamento = input('Qual será a forma de pagamento? ')
desc10 = produto / 10
desc5 = produto / 20
juros20 = produto / 5
if formaDePagamento == '1':
    print('Valor a pagar {:.1f}'.format(produto - desc10))
elif formaDePagamento == '2':
    print('Valor a pagar {:.1f}'.format(produto - desc5))
elif formaDePagamento == '3':
    print('Valor a pagar {}'.format(produto))
elif formaDePagamento == '4':
    parcelas = int(input('Quantas parcelas? '))
    print('Valor a pagar {:.1f} em {} parcelas de {:.1f}'.format(produto + juros20, parcelas,
                                                                 (produto + juros20) / parcelas))