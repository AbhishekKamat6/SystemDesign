from beverage.base import Beverage
from models.enums import DrinkType
from models.reciepe import Reciepe
from models.enums import Ingredient
from dataclasses import dataclass


@dataclass(slots=True)
class BaseBeverage(Beverage):
    drink_type : DrinkType
    reciepe : Reciepe

    @property
    def cost(self):
        return self.reciepe.price

    @property
    def needs(self)->dict[Ingredient,int]:
        return dict(self.reciepe.needs) # fresh copy

    @property
    def description(self)->str:
        return self.drink_type.name


