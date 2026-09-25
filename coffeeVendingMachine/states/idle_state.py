
from states.base import MachineState
from exceptions.exception import InvalidAmountException , IllegalStateException

class IdleState(MachineState):

    def insert_money(self,machine,amount):
        if amount <= 0 :
            raise InvalidAmountException(amount)

        machine.add_balance(amount)

        from states.has_money_state import HasMoneyState

        machine.state = HasMoneyState()

    def select_drink(self,machine,drink_type,addons):
        raise IllegalStateException("Insert money first")

    def dispense(self, machine):
        raise IllegalStateException("No item to dispense")

    def refund(self, machine):
        raise IllegalStateException("No money to refund")

    