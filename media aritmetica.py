print('Olá estudante!')
print('Está pronto para ver se passou de ano? Vamos lá!')
n1=float(input('digite sua primeira nota: '))
n2=float(input('digite sua segunda nota: '))
media= (n1+n2)/2
print(f'Sua média final é: {media}')
if media >=6:
    print(f'Parabéns! você foi aprovado. Aproveite suas férias!')
else:
    print(f'Infelizmente, você foi reprovado. Mas não desista! continue tentando! ')