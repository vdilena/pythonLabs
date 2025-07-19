#Clase concreta(recibe por parametro la clase de la que extiende)
from objetos.personas.Persona import Persona
from objetos.interfaces.Aportante import Aportante


class Empleado(Persona, Aportante):

    # Sobrescritura de metodo ejecutarAccion
    def ejecutarAccion(self):
        return f'{super().ejecutarAccion() + 'trabajar'}'
    
    # Implementacion del metodo pagarImpuestos
    def pagarImpuestos(self):
        print('El empleado paga impuestos normalmente')

    # Implementacion del metodo pagarAportesSueldo
    def pagarAportesSueldo(self):
        print('El empleado hace aportes normalmente')