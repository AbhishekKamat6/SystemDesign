from abc import ABC , abstractmethod
from models.enums import IngredientType

class Base(ABC):

    @property
    @abstractmethod
    def needs(self)->dict[IngredientType,int]:
        pass

    @property
    @abstractmethod
    def cost(self):
        pass

    @property
    @abstractmethod
    def description(self):
        pass