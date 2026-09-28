from states.base import State
from exceptions.exception import InvalidAmountException , InvalidStateException
from states.validate_and_select import ValidateAndSelect

class IdleState(State):

    def insert_money(self, machine, amount):
       if amount < 0 :
           raise InvalidAmountException("Amount cannot be less than 0")
       machine.balance = amount
       machine.state = ValidateAndSelect()

    def validate_and_select(self, machine):
        raise InvalidStateException("First insert money")

    def dispense(self, machine):
        raise InvalidStateException("Item should be selected before dispense")

    def refund(self, machine):
        raise InvalidStateException("Cannot refund before inserting money")