from dataclasses import dataclass , field
from models.reciepe import ReciepeBook
from states.base import State
from states.idle_state import IdleState
from inventory.inventory import Inventory
from models.enums import DrinkType , Addons


@dataclass(slots=True)
class CoffeeMachine:

    balance : int = field(default=0)
    _pending : object  = field(default_factory=object)
    _pending_needs : dict = field(default_factory=dict)
    book : ReciepeBook = field(default_factory=ReciepeBook)
    inventory : Inventory = field(default_factory=Inventory)
    _state : State = field(default_factory=IdleState)

    @property
    def pending(self):
        return self._pending
    
    @property
    def pending_needs(self):
        return self._pending_needs

    @pending.setter
    def pending(self,value):
        self._pending = value

    @pending_needs.setter
    def pending_needs(self,value):
        self._pending_needs = value
    
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self,value):
        self._state = value

    def add_recipe(self,drink_type,ingredients):
        self.book.add_recipe(drink_type,ingredients)

    # customer facing
    def insert_money(self,amount):
        self._state.insert_money(self,amount)

    def validate_and_select(self,drink_type:DrinkType,addons:list[Addons]):
        self._state.validate_and_select(self,drink_type,addons)

    def dispense(self):
        self._state.dispense(self)
   
    # callbacks
    def brew_hardware(self):
        print(f"done brewing , {self._pending.description}")
    
    def give_change(self,amount):
        print(f"amount returned {amount}")

    def set_pending(self,beverages,ingredients):
        self._pending = beverages
        self._pending_needs = ingredients

    # operators

    def refill(self,ingredient_type,quantity):
        self.inventory.add(ingredient_type,quantity)
    