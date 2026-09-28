from dataclasses import dataclass , field
from models.enums import DrinkType , IngredientType
from exceptions.exception import RecipeNotFoundException

@dataclass(slots=True)
class Recipe:
    price : int
    ingredient : dict[IngredientType,int] = field(default_factory=dict)


@dataclass(slots=True)
class ReciepeBook:
    recipe : dict[DrinkType,Recipe] = field(default_factory=dict)

    def add_recipe(self,drink_type:DrinkType,recipe:Recipe):
        self.recipe[drink_type] = recipe

    def get_recipe(self,drink_type):
        recipe = self.recipe.get(drink_type)

        if recipe is None:
            raise RecipeNotFoundException("reciepe not found")

        return recipe




