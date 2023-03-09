print('''
Digite um número inteiro
Caso você digite um valor que não seja inteiro o resultado dará erro 😑
''')

def erro(valor):
     try:
        valor == int(valor)
        print('O valor é válido')
     except ValueError:
         print('Erro! Digite um valor válido')

valor = input('Digite o valor:')
erro(valor)
