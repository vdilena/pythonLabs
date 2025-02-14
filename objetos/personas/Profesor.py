from .Persona import Persona
from objetos.interfaces.Aprendiz import Aprendiz


class Profesor(Persona, Aprendiz):

    # Sobrescritura de metodo ejecutarAccion
    def ejecutarAccion(self):
        return f'{super().ejecutarAccion() + 'enseñar'}'
    
    # Implementacion del metodo aprenderIdioma
    def aprenderIdioma(self):
        print('El profesor aprende idioma en por su cuenta')

    # Implementacion del metodo aprenderSobreCiencia
    def aprenderSobreCiencia(self):
        print('El profesor aprende ciencia en la universidad a traves de la investigacion')