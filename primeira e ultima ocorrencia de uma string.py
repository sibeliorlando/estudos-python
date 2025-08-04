frase=str(input('digite uma frase: ')).upper().strip()
print(f'a letra A aparece {frase.count('A')} vezes na sua frase')
print(f'a primeira letra A aparece na posicao {frase.find('A')+1}')
print(f'a ultima letra A aparece na posicao {frase.rfind('A')+1}')