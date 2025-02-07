from abc import abstractmethod
# Clase abstracta Persona y sus clases concretas Empleado, Alumno, Profesor y Deportista
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

#Clase concreta(recibe por parametro la clase de la que extiende)
class Empleado(Persona):

    # Sobrescritura de metodo ejecutarAccion
    def ejecutarAccion(self):
        return f'{super().ejecutarAccion() + 'trabajar'}'
    
class Alumno(Persona):

    # Sobrescritura de metodo ejecutarAccion
    def ejecutarAccion(self):
        return f'{super().ejecutarAccion() + 'estudiar'}'
    
class Profesor(Persona):

    # Sobrescritura de metodo ejecutarAccion
    def ejecutarAccion(self):
        return f'{super().ejecutarAccion() + 'enseñar'}'
    
class Deportista(Persona):

    # Sobrescritura de metodo ejecutarAccion
    def ejecutarAccion(self):
        return f'{super().ejecutarAccion() + 'entrenar'}'
    
# Clase con metodos estaticos
class Calculadora:

    @staticmethod
    def sumar(a,b):
        return a + b
    
    @staticmethod
    def restar(a,b):
        return a - b
    
    @staticmethod
    def multiplicar(a,b):
        return a * b
    
    @staticmethod
    def dividir(a,b):
        return a / b
    
    @staticmethod
    def potencia(a,b):
        return pow(a, b)
    
#Instacia de clases
empleado = Empleado('Mariela', 'Gimenez')
alumno = Alumno('Carolina', 'Suarez')
profesor = Profesor('Juan', 'Perez')
deportista = Deportista('Jose', 'Blanco')

#Ejecucion de metodos no estaticos
empleado.displayDatosPersonales()
alumno.displayDatosPersonales()
profesor.displayDatosPersonales()
deportista.displayDatosPersonales()

#Ejecucion de metodos estaticos
suma = Calculadora.sumar(3,5)
resta = Calculadora.restar(6,4)
multiplicacion = Calculadora.multiplicar(8,2)
division = Calculadora.dividir(9,3)
potencia = Calculadora.potencia(2,3)

print(f'Suma: {suma}')
print(f'Resta: {resta}')
print(f'Multplicacion: {multiplicacion}')
print(f'Division: {division}')
print(f'Potencia: {potencia}')

#Gestion de properties (getters y setters)
empleado.nombre = 'Mariela Julieta'
empleado.apellido = 'Gimenez Gonzalez'
empleado.displayDatosPersonales()

#Polimorfismo
personas = [empleado, alumno, profesor, deportista]
for persona in personas:
    print(f'{persona.ejecutarAccion()}')

#Interfaces