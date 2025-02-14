#Instacia de clases
from .Alumno import Alumno
from .Deportista import Deportista
from .Empleado import Empleado
from .Profesor import Profesor

empleado = Empleado('Mariela', 'Gimenez')
alumno = Alumno('Carolina', 'Suarez')
profesor = Profesor('Juan', 'Perez')
deportista = Deportista('Jose', 'Blanco')

#Ejecucion de metodos
empleado.displayDatosPersonales()
empleado.pagarAportesSueldo()
alumno.displayDatosPersonales()
alumno.aprenderIdioma()
alumno.aprenderSobreCiencia()
profesor.displayDatosPersonales()
profesor.aprenderSobreCiencia()
deportista.displayDatosPersonales()
deportista.pagarImpuestos()

#Gestion de properties (getters y setters)
empleado.nombre = 'Mariela Julieta'
empleado.apellido = 'Gimenez Gonzalez'
empleado.displayDatosPersonales()

#Polimorfismo
personas = [empleado, alumno, profesor, deportista]
for persona in personas:
    print(f'{persona.ejecutarAccion()}')