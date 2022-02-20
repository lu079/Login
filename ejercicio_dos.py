"""
1. Defina una clase Libro con los siguientes atributos: Título, Autor (Nombre), Precio y Likes (por defecto inicializado en cero).
2. Defina un constructor utilizado para inicializar los atributos del método con valores ingresados por el usuario.
3. Configure un método view() para mostrar información del libro actual.
4. Configure un método like() para indicar que un libro le gusta.
5. Configure un método dilike() para indicar que un libro no le gusta.
6. Escriba un programa para probar la clase Book.
"""

titulo=(input('Nombre del Libro: '))
autor=(input('Nombre del Autor: '))
precio=int(input('Precio: '))

class Book:
    titulo=''
    autor=''
    precio=''
    likes=True

    def view(self):
        return f'\n Los datos ingresados son: \n Titulo: {titulo} \n Autor: {autor} \n Precio: {precio} \n '

    # for item in likes:
        # if likes == True:
    def like(self):
        self.likes=True
        return f'Me gusta el libro {titulo}.'
        # else:
    def dislike(self):
        self.likes=False
        return f'No me gusta la forma de escribir de {autor}.'

libro=Book()
# print(libro.titulo)

print(libro.view())
print(libro.like())
print(libro.dislike())

