
from state.atm_state import AtmState
from exception.exceptions import IllegalStateException

class DispensedState(AtmState):
    def insert_card(self, atm, card): raise IllegalStateException("Dispensing in progress")
    def enter_pin(self, atm, pin): raise IllegalStateException("Dispensing in progress")
    def withdraw(self, atm, amount): raise IllegalStateException("Dispensing in progress")
    def check_balance(self, atm): raise IllegalStateException("Dispensing in progress")

    def eject_card(self, atm):
        from state.idle_state import IdleState
        notes = atm.dispenser.dispense(atm.pending_amount)
        atm._last_dispensed_notes = notes
        atm._return_card()
        atm._set_state(IdleState())