from abc import ABC
from abc import abstractmethod

# Clase de tipo interface
class Aportante(ABC):
    
    @abstractmethod
    def pagarImpuestos(self):
        pass
    
    @abstractmethod
    def pagarAportesSueldo(self):
        pass
