from abc import ABC
from abc import abstractmethod

class Aprendiz(ABC):

    @abstractmethod
    def aprenderIdioma(self):
        pass

    @abstractmethod
    def aprenderSobreCiencia(self):
        pass
