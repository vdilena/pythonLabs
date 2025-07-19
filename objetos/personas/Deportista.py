from objetos.personas.Persona import Persona
from objetos.interfaces.Aportante import Aportante


class Deportista(Persona, Aportante):

    # Sobrescritura de metodo ejecutarAccion
    def ejecutarAccion(self):
        return f'{super().ejecutarAccion() + 'entrenar'}'
    
    # Implementacion del metodo pagarImpuestos
    def pagarImpuestos(self):
        print('El deportista paga impuestos con descuento')

    # Implementacion del metodo pagarAportesSueldo
    def pagarAportesSueldo(self):
        print('El deportista hace aportes con descuento')