#Array

libros = ["Harry Potter", "Boulevard"]
print(libros)
 
nombres = [ "Jose", "Hasley"]

print(nombres)


#Objeto

class ciudad_Tokio:
    def __init__(self, poblacion, clima,ruta):
        self.poblacion = poblacion
        self.clima = clima
        self.ruta = ruta
        
ciudad_Tokio = ( 15000, 'calido', 'facil')
print(ciudad_Tokio)