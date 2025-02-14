from objetos.personas.Persona import Persona
from objetos.interfaces.Aprendiz import Aprendiz


class Alumno(Persona, Aprendiz):

    # Sobrescritura de metodo ejecutarAccion
    def ejecutarAccion(self):
        return f'{super().ejecutarAccion() + 'estudiar'}'
    
    # Implementacion del metodo aprenderIdioma
    def aprenderIdioma(self):
        print('El alumno aprende idioma en la escuela')

    # Implementacion del metodo aprenderSobreCiencia
    def aprenderSobreCiencia(self):
        print('El alumno aprende ciencia en la escuela')