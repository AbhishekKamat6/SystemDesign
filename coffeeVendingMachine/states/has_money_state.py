from dataclasses import dataclass
from states.base import MachineState
from beverage.base_beverage import BaseBeverage
from beverage.addons import ExtraMilk , ExtraSugar
from models.enums import AddOn
from exceptions.exception import InsufficientBalanceException

@dataclass(slots=True)
class HasMoneyState(MachineState):

    def insert_money(self,machine,amount):
        machine.add_balance(amount)

    def select_drink(self,machine,drink_type,addons):
        beverage = BaseBeverage(drink_type,machine.book.recipe_for(drink_type))

        for addon in addons:
            beverage = self._decorate(beverage,addon)

        if machine.balance < beverage.cost : 
            raise InsufficientBalanceException(beverage.cost,machine.balance)

        needs = beverage.needs
        if not machine.book.has_ingredients(needs):
            raise InsufficientBalanceException(beverage.cost,machine.balance)


    def _decorate(self,beverage,addon:AddOn):

        match addon :
            case AddOn.EXTRA_MILK:
                return ExtraMilk(beverage)
            case AddOn.EXTRA_SUGAR :
                return ExtraSugar(beverage)
            case _:
                raise ValueError(addon)
