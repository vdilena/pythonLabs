from abc import abstractmethod

# Clase abstracta Persona
class Persona:

    # Constructor
    def __init__(self, nombre, apellido):

        #Definicion de atributos
        self.__nombre = nombre
        self.__apellido = apellido

    # Getters
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    # Setters
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    # Metodo concreto (se pasa por parametro el objeto que ejecuta el metodo)
    def displayDatosPersonales(self):
        print(f'{self.nombre + ' ' + self.apellido}')

    def displayActividad(self):
        print(f'{self.ejecutarAccion()}')

    # Metodo abstracto
    @abstractmethod
    def ejecutarAccion(self):
        return f'El {type(self).__name__} va a '