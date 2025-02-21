from abc import ABC, abstractmethod

# Clase base abstracta para los empleados
class Empleado(ABC):
    @abstractmethod
    def realizar_actividad(self) -> str:
        pass

# Clases concretas para cada tipo de empleado

class Medico(Empleado):
    def realizar_actividad(self) -> str:
        return "Atendiendo a pacientes y realizando procedimientos médicos."

class Economista(Empleado):
    def realizar_actividad(self) -> str:
        return "Analizando el mercado y elaborando pronósticos económicos."

class IngenieroSoftware(Empleado):
    def realizar_actividad(self) -> str:
        return "Desarrollando software y solucionando problemas técnicos."

class Docente(Empleado):
    def realizar_actividad(self) -> str:
        return "Enseñando en el aula y preparando material educativo."

# Clase abstracta para la fábrica de empleados
class EmpleadoFactory(ABC):
    @abstractmethod
    def crear_empleado(self, tipo: str) -> Empleado:
        pass

# Implementación concreta de la fábrica de empleados
class EmpleadoFactoryConcreto(EmpleadoFactory):
    def crear_empleado(self, tipo: str) -> Empleado:
        if tipo == "Medicina":
            return Medico()
        elif tipo == "Economía":
            return Economista()
        elif tipo == "Ingeniero de software":
            return IngenieroSoftware()
        elif tipo == "Docente":
            return Docente()
        else:
            raise ValueError(f"Tipo de empleado '{tipo}' no reconocido.")

# Ejemplo de uso
factory = EmpleadoFactoryConcreto()

tipos = ["Medicina", "Economía", "Ingeniero de software", "Docente"]

for tipo in tipos:
    empleado = factory.crear_empleado(tipo)
    print(f"{tipo}: {empleado.realizar_actividad()}")
