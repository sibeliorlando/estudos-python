print('='*3,'REAJUSTE SALARIAL 15%','='*3)
atual=float(input('digite seu salário atual: '))
reajuste= atual*15/100
print(f'O aumento salarial em reais do seu salario é de: R${reajuste}')
print(f'Ou seja, seu novo salário é: R${atual+reajuste}')
