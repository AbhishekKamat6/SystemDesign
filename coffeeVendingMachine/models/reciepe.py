from dataclasses import dataclass , field
from models.enums import Ingredient
from models.enums import DrinkType
from exceptions.exception import UnknownDrinkException

@dataclass(slots=True,frozen=True)
class Reciepe : 
   needs : dict[Ingredient,int]
   price : int

   def __post_init__(self)->None:
      object.__setattr__(self,"needs",dict(self.needs))

@dataclass(slots=True)
class ReciepeBook:

   book : dict[DrinkType,Reciepe] = field(default_factory=dict)

   def add(self,drink_type:DrinkType,reciepe:Reciepe)->None:
      self.book[drink_type] = reciepe

   def get_reciepe(self,drink_type:DrinkType):
      reciepe = self.book.get(drink_type) 
      if reciepe is None:
        raise UnknownDrinkException(drink_type)
      return reciepe
    



# Here is the reason why we need copy 

# # --- WITHOUT the defensive copy ---
# class RecipeNoCopy:
#     def __init__(self, needs, price):
#         self.needs = needs   # just grabs the SAME dict, no copy
#         self.price = price

# # building a latte recipe
# base = {'WATER': 100, 'MILK': 150, 'BEANS': 18}
# latte = RecipeNoCopy(base, price=140)

# # now building cappuccino, starting from the same base and tweaking it
# base['MILK'] = 60   # 'just adjusting milk for the cappuccino version'
# cappuccino = RecipeNoCopy(base, price=120)

# print('latte needs:', latte.needs)
# print('cappuccino needs:', cappuccino.needs)
# Output

# latte needs:      {'WATER': 100, 'MILK': 60, 'BEANS': 18}
# cappuccino needs: {'WATER': 100, 'MILK': 60, 'BEANS': 18}

# Look at that output: the latte's milk silently became 60 too. You never touched latte — you only wrote base['MILK'] = 60, 
# meaning to set up the cappuccino. But latte.needs and base were never two separate things — latte.needs was just another name for the exact same dict. So editing "the cappuccino's numbers" edited the latte at the same time, because there was only ever one dict, wearing two labels.
# If this shipped, every latte the machine ever poured from then on would use 60ml of milk

