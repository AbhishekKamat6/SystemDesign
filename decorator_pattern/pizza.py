from abc import ABC,abstractmethod

class Pizza(ABC):
    @property
    @abstractmethod
    def cost(self):
        pass

    @property
    @abstractmethod
    def desc(self):
        pass

