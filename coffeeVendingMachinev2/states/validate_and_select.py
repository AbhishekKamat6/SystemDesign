from typing import TYPE_CHECKING

from states.base import State
from exceptions.exception import InvalidAmountException,InvalidStateException,InSufficientBalanceException , IngredientUnavailableException
from models.enums import DrinkType,Addons
from beverages.base_beverage import BaseBeverage
from beverages.addons import ExtraMilk , ExtraSugar

if TYPE_CHECKING:
    from coffee_machine import CoffeeMachine

class ValidateAndSelect(State):

    def insert_money(self, machine, amount):
       if amount < 0 :
           raise InvalidAmountException("Amount cannot be less than 0")
       # update the state
       machine.state = ValidateAndSelect()

    def _decorator(self,beverage,add_on):
        match add_on :
            case Addons.EXTRA_MILK :
                return ExtraMilk(beverage)
            case Addons.EXTRA_SUGAR : 
                return ExtraSugar(beverage)


    def validate_and_select(self, machine:"CoffeeMachine" , drink_type:DrinkType , addons:list[Addons] ):

        beverage = machine.book.get_recipe(drink_type)

        beverage = BaseBeverage(drink_type,beverage)

        for add_on in addons:
            beverage = self._decorator(beverage,add_on)

        if machine.balance < beverage.cost :
            InSufficientBalanceException()

        needs = beverage.needs

        if not machine.inventory.try_dispensing(needs):
            return IngredientUnavailableException("Required ingredients are not available")

        from states.dispense_state import DispenseState
        machine.pending = beverage
        machine.pending_needs = beverage.needs
        machine.state = DispenseState()

        machine.dispense()


        

    def dispense(self, machine):
        raise InvalidStateException("Item should be selected before dispense")

    def refund(self, machine):
        raise InvalidStateException("Cannot refund before inserting money")