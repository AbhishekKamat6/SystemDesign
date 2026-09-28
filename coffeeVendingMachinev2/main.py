from coffee_machine import CoffeeMachine
from models.reciepe import ReciepeBook , Recipe
from models.enums import DrinkType , IngredientType , Addons



cm = CoffeeMachine()

ingredients = Recipe(200,{IngredientType.MILK:100,IngredientType.SUGAR:5})
recipe = ReciepeBook({DrinkType.ESPRESSO:ingredients})

cm.refill(IngredientType.MILK,500)
cm.refill(IngredientType.SUGAR,500)

cm.add_recipe(DrinkType.ESPRESSO,ingredients)

cm.insert_money(250)

cm.validate_and_select(DrinkType.ESPRESSO,[Addons.EXTRA_MILK,Addons.EXTRA_SUGAR])




