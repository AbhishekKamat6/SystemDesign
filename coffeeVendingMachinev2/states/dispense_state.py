from states.base import State
from states.validate_and_select import ValidateAndSelect
from exceptions.exception import InvalidAmountException,InvalidStateException,InSufficientBalanceException , IngredientUnavailableException
from models.enums import DrinkType,Addons
from coffee_machine import CoffeeMachine
from beverages.base_beverage import BaseBeverage
from beverages.addons import ExtraMilk , ExtraSugar


class DispenseState(State):

    def insert_money(self, machine, amount):
       if amount < 0 :
           raise InvalidAmountException("Amount cannot be less than 0")
       # update the state
       machine.state = ValidateAndSelect()

    def validate_and_select(self, machine:CoffeeMachine , drink_type:DrinkType , addons:list[Addons] ):
        raise InvalidStateException("Item i already in dispense state")

    def dispense(self, machine:CoffeeMachine):
         machine.brew_hardware()
         machine.give_change(machine.balance - machine.pending.cost)

    def refund(self, machine):
        raise InvalidStateException("Cannot refund before inserting money")