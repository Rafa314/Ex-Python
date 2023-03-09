print('''
Descobrirei se o valor é NaN ou não . 😁
''')

import math
def Nao_numero(value):
    isNaN = math.isnan(value)
    if isNaN == True:
         print("O valor é NaN")
    else:
        print("O valor não é NaN")

Nao_numero(0)