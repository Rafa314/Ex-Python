print('''
Descobrirei se o valor é booleano ou não . 😁
''')
def e_booleano(valor):
    if valor == bool(valor):
        print('O valor {} é booleano'.format(valor))
    else:
        print('O valor {} não é booleano'.format(valor))

e_booleano(3)
