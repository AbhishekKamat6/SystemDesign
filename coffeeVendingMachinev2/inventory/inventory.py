from dataclasses import dataclass , field
from models.enums import IngredientType
from models.reciepe import Recipe
from exceptions.exception import QuantityNotAvailableException
import threading


@dataclass(slots=True)
class Inventory:

    stock : dict[IngredientType,int]  = field(default_factory=dict)
    _lock : threading.Lock = field(default_factory=threading.Lock)


    def try_dispensing(self,needs:dict[IngredientType,int]):

        with self._lock:
            for ingredient , quantity in needs.items():
              if self.stock.get(ingredient,0) < quantity : 
                return False

            for ingredient , quantity in needs.items():
              self.stock[ingredient] = self.stock.get(ingredient,0) - quantity

            return True

                

    def add(self,ingredient_type,quantity):
        with self._lock:
           self.stock[ingredient_type] = self.stock.get(ingredient_type,0) + quantity