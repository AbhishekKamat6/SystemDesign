from dataclasses import dataclass , field
from models.enums import Ingredient
import threading

@dataclass(slots=True)
class IngredientInventory:

    stock : dict[Ingredient,int] = field(default_factory=dict)
    lock: threading.Lock = field(default_factory=threading.Lock, repr=False)

    def try_reserve(self,needs:dict[Ingredient,int])->bool:

        with self.lock : 
            for ingredient , quantity in needs.items():
                if self.stock.get(ingredient,0) < quantity :
                    return False

            for ingredient , quantity in needs.items():
                self.stock[ingredient] = self.stock.get(ingredient,0) - quantity

            return True


    def refill(self,ingredient:Ingredient,units:int)->None:
        with self.lock:
            self.stock[ingredient] = self.stock.get(ingredient,0) + units

    def level(self,ingredient:Ingredient)->int:
        with self.lock :
         return self.stock.get(ingredient,0)        