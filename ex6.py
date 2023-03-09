print(''' Este exercício é um exemplo de como o paradigma de poo presente se aplica em python :
 basicamente os valores do Python funcionam como objetos de determinadas classes --- no entanto podemos fazer 
 a mesma coisa como definir classes
   ''')
#Primeiro definimos a classe Cachorro onde obviamente os objetos serão diferenciados por atributos como nesse caso nome
class Cachorro:

    tipo = 'canino'

    def __init__(self, nome):
        self.nome = nome

a = Cachorro('Fido')
b = Cachorro('Mel')


print('O nome do cachorro a é {}'.format(a.nome))
print('A classe do cachorro a é {} \n'.format(type(a)))
print('O nome do cachorro b é {}'.format(b.nome))
print('A classe do cachorro b é {} '.format(type(b)))

print('Perceba que a classe de ambos é __main__.Cachorro')

