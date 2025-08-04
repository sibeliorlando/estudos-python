print('='*3, 'CALCULANDO DESCONTOS', '='*3)
n=float(input('digite o valor do seu produto: '))
v=int(input('qual foi o valor do seu desconto? '))
d= n*v/100
print(f'o valor em reias do desconto é:{d} ')
print(f'ou seja, você irá pagar no seu produto o valor de: R${n-d}')
