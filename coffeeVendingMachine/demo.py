from coffee_machine import CoffeeMachine
from models.enums import Ingredient , DrinkType , AddOn
from models.reciepe import Reciepe

m = CoffeeMachine()

m.book.add(
    DrinkType.CAPUCCINO,
    Reciepe({ Ingredient.WATER : 100 , Ingredient.MILK : 60 , Ingredient.BEANS : 18 },120)
)

m.refill(Ingredient.WATER, 2000)
m.refill(Ingredient.MILK, 500)
m.refill(Ingredient.BEANS, 300)
m.refill(Ingredient.SUGAR,500)

m.insert_money(1200)
m.select_drink(DrinkType.CAPUCCINO,[AddOn.EXTRA_MILK])

