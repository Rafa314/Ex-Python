print('''
Descobrirei se o valor é número ou não . 😁
''')

def numero_ou_nao(valor):
    try:
      if valor == int(valor):
          print('O valor é número')
    except:
        if ValueError:
            print('Não é número')

numero_ou_nao(5)
