from dataclasses import dataclass
from states.base import MachineState
from beverage.base_beverage import BaseBeverage
from beverage.addons import ExtraMilk , ExtraSugar
from models.enums import AddOn
from exceptions.exception import InsufficientBalanceException , IngredientUnavailableException , IllegalStateException

@dataclass(slots=True)
class HasMoneyState(MachineState):

    def insert_money(self,machine,amount):
        machine.add_balance(amount)

    def select_drink(self,machine,drink_type,addons):
        beverage = BaseBeverage(drink_type,machine.book.get_reciepe(drink_type))

        for addon in addons:
            beverage = self._decorate(beverage,addon)

        if machine.balance < beverage.cost : 
            raise InsufficientBalanceException(beverage.cost,machine.balance)

        needs = beverage.needs
        if not machine.inventory.try_reserve(needs):
            raise IngredientUnavailableException(needs)

        machine.set_pending(beverage,needs)

        from states.brewing_state import BrewingState

        machine.state = BrewingState()
        machine.dispense()


    def _decorate(self,beverage,addon:AddOn):

        match addon :
            case AddOn.EXTRA_MILK:
                return ExtraMilk(beverage)
            case AddOn.EXTRA_SUGAR :
                return ExtraSugar(beverage)
            case _:
                raise ValueError(addon)

    
    def dispense(self, machine):
        raise IllegalStateException("Select a drink first")

    
    def refund(self, machine):
        machine.refund_balance()

        from states.idle_state import IdleState
        machine.state = IdleState()