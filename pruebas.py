# Se ejecuta desde la consola con el comando py .\pruebas.py

from objetos.personas.Alumno import Alumno
from objetos.personas.Deportista import Deportista
from objetos.personas.Empleado import Empleado
from objetos.personas.Profesor import Profesor


#Instacia de clases
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