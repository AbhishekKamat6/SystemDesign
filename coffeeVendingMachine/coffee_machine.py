
from inventory.ingredient_inventory import IngredientInventory
from states.base import MachineState
from states.idle_state import IdleState
from models.reciepe import ReciepeBook
from models.enums import Ingredient
from models.reciepe import Reciepe

from dataclasses import dataclass , field


@dataclass(slots=True)
class CoffeeMachine:
     inventory : IngredientInventory = field(default_factory=IngredientInventory)
     book : ReciepeBook = field(default_factory=ReciepeBook)
     _state : MachineState = field(default_factory=IdleState)
     _balance : int = field(default=0)
     _pending : object = field(default=None)
     _pending_needs : dict | None = field(default=None)

     @property
     def state(self):
        return self._state

     @state.setter
     def state(self,value):
        self._state = value

     @property
     def balance(self)->int:
        return self._balance

     @property
     def pending_cost(self)->int:
        return self._pending.cost

     @property
     def pending_needs(self)->dict:
        return self._pending_needs

     # Customer Facing
     def insert_money(self,amount):
        self._state.insert_money(self,amount)

     def select_drink(self,drink_type,addons):
        self._state.select_drink(self,drink_type,addons)

     def dispense(self)->None:
        self._state.dispense(self)

     def refund(self)->None:
        self._state.refund(self)

    # Operator facing
     def refill(self,ingredient:Ingredient,units:int)->None:
        self.inventory.refill(ingredient,units)

     def add_reciepe(self,drink_type,reciepe:Reciepe):
        self.book.add(drink_type,reciepe)

    # callbacks used by states
     def add_balance(self,amount):
        self._balance += amount

     def set_pending(self,beverage,needs:dict[Ingredient,int])->None:
        self._pending = beverage
        self._pending_needs = needs

     def give_change(self,change:int):
        if change > 0 :
           print(f"change : {change}")

     def refund_balance(self) -> None:
        if self._balance > 0:
            print(f"Refund: {self._balance}")
        self._balance = 0

     def brew_hardware(self) -> None:
        print(f"Brewing: {self._pending.description}")

     def reset(self) -> None:
        self._balance = 0
        self._pending = None
        self._pending_needs = None

     


