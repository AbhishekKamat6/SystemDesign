from states.base import MachineState
from exceptions.exception import IllegalStateException , BrewFailureException

from dataclasses import dataclass

@dataclass(slots=True)
class BrewingState(MachineState):
    def insert_money(self, machine, amount):
        raise IllegalStateException("Brewing in progress")

    def select_drink(self, machine, drink_type, addons):
        raise IllegalStateException("Brewing in progress")

    def refund(self, machine):
        raise IllegalStateException("Brewing in progress")

    def dispense(self, machine):
        try:
            machine.brew_hardware()
            machine.give_change(machine.balance - machine.pending_cost)
        except BrewFailureException:
            machine.inventory.release(machine.pending_needs)  # compensation
            machine.refund_balance()
        finally:
            machine.reset()

            from states.idle_state import IdleState
            machine.state = IdleState()