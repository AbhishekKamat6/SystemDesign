from abc import ABC , abstractmethod
from models.enums import Ingredient


class Beverage(ABC):

    @property
    @abstractmethod
    def cost(self)->int:
        pass

    @property
    @abstractmethod
    def needs(self)->dict[Ingredient,int]:
        pass

    property
    @abstractmethod
    def description(self)->str:
        pass

