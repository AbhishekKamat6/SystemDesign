
from beverage.beverage_decorator import BeverageDecorator
from models.enums import Ingredient
from dataclasses import dataclass


@dataclass(slots=True)
class ExtraMilk(BeverageDecorator):

    @property
    def cost(self)->int:
        return self.inner.cost + 20

    @property
    def needs(self)->dict[Ingredient,int]:
        n = self.inner.needs
        n[Ingredient.MILK] = n.get(Ingredient.MILK,0) + 30
        return n

    @property
    def description(self):
        return print(f"{self.inner.description} + extra milk")

@dataclass(slots=True)
class ExtraSugar(BeverageDecorator):

    @property
    def cost(self)->int:
        return self.inner.cost + 10

    @property
    def needs(self)->dict[Ingredient,int]:
        n = self.inner.needs
        n[Ingredient.SUGAR] = n.get(Ingredient.SUGAR,0) + 5 
        return n 

    @property
    def description(self) -> str:
        return f"{self.inner.description} + extra sugar"