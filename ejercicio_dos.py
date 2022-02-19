"""
1. Defina una clase Libro con los siguientes atributos: Título, Autor (Nombre), Precio y Likes (por defecto inicializado en cero).
2. Defina un constructor utilizado para inicializar los atributos del método con valores ingresados por el usuario.
3. Configure un método view() para mostrar información del libro actual.
4. Configure un método like() para indicar que un libro le gusta.
5. Configure un método dilike() para indicar que un libro no le gusta.
6. Escriba un programa para probar la clase Book.
"""

# cantidad=int(print('Cuántos libros desea ingresar: '))
titulo=(input('Nombre del Libro: '))
autor=(input('Nombre del Autor: '))
precio=int(input('Precio: '))
likes=int(input('Cantidad de likes que recibe: '))

visualizar=(input('Desea ver los valores agregados?: S/N ')).capitalize()
class Book:
    def __init__(self,titulo='',autor='',precio='',likes=''):
        self.titulo=titulo
        self.autor=autor
        self.precio=precio
        self.likes=likes
    def view(self):
        return f'{self.titulo} \n Autor: {self.autor} \n Precio: {self.precio} \n Likes: {self.likes}'

    def like(self):
        return f'Me gusta el libro {self.titulo}.'

    def dislike(self):
        return f'No me gusta la forma de escribir de {self.autor}.'

print(titulo.view())


