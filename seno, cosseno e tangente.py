import math
a=float(input('digite o angulo desejado: '))
s= math.sin((math.radians(a)))
print(f'o seno de {a} é {s:.2f}')
c= math.cos((math.radians(a)))
print(f'o cosseno de {a} é {c:.2f}')
t= math.tan(math.radians(a))
print(f'a tagente de {a} é {t:.2f}')

