ca= float(input('digite o valor do comprimento do cateto adjacente: '))
co= float(input('digite o valor do comprimento do cateto oposto: '))
hi= (ca**2 + co**2) **(1/2)
print(f'a hipotenusa vai medir {hi:.2f}')

import math
co= float(input('digite o valor do comprimento do cateto oposto: '))
ca= float(input('digite o valor do comprimento do cateto adjacente: '))
hi= (math.hypot(co, ca))
print(f'a hipotenusa mede {hi:.2f}')