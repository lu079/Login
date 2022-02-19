"""
1. Defina una clase Libro con los siguientes atributos: Título, Autor (Nombre), Precio y Likes (por defecto inicializado en cero).
2. Defina un constructor utilizado para inicializar los atributos del método con valores ingresados por el usuario.
3. Configure un método view() para mostrar información del libro actual.
4. Configure un método like() para indicar que un libro le gusta.
5. Configure un método dilike() para indicar que un libro no le gusta.
6. Escriba un programa para probar la clase Book.
"""

# cantidad=int(print('Cuántos libros desea ingresar: '))
ti=(input('Nombre del Libro: '))
au=(input('Nombre del Autor: '))
pre=int(input('Precio: '))
like=int(input('Cantidad de likes que recibe: '))

visualizar=(input('Desea ver los valores agregados?: S/N ')).capitalize()
class Book:
    def __init__(self,titulo,autor,precio,likes):
        self.titulo=titulo
        self.autor=autor
        self.precio=precio
        self.likes=likes

    def view(self):
        return f"\n La información es la siguiente: \n Titulo: {self.titulo} \n Autor: {self.autor} \n Precio: {self.precio} \n Likes: {self.likes}
        # for item in visualizar:
        #     if item== 'S':
        #         print(f"\n La información es la siguiente: \n Titulo: {self.titulo} \n Autor: {self.autor} \n Precio: {self.precio} \n Likes: {self.likes}")
        #         print('En un momento se imprimirá su factura.')
        #     if visualizar== 'N':
        #         print(f"\n Gracias por ingresar los datos. En un momento se imprimirá su factura.")
            # if self.titulo== 'tres':
            #     print(f"La información es la siguiente: \n Titulo: {self.titulo} \n Autor: {self.autor} \n Precio: {self.precio} \n Likes: {self.likes}")

    def like(self):
        pass

    def dislike(self):
        pass

    def __str__(self):
        pass


ti=titulo()
# au=(input('Nombre del Autor: '))
# pre=int(input('Precio: '))
# like=

# visualizar.view()
