from dataclasses import dataclass
from beverages.beverage_decorator import BeverageDecorator
from models.enums import DrinkType , IngredientType
from models.reciepe import Recipe
from beverages.base import Base


@dataclass(slots=True)
class BaseBeverage(Base):

    drinktype : DrinkType
    recipe : Recipe

    @property
    def cost(self):
       return self.recipe.price

    @property
    def needs(self)->dict[IngredientType,int]:
       return dict(self.recipe.ingredient)

    @property
    def description(self):
       return self.drinktype.name + " with "

    




