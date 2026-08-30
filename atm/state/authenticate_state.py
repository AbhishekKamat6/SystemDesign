from __future__ import annotations

from exception.exceptions import IllegalStateException , InvalidAmountException , InsufficientCashException
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from atm import Atm

from state.dispense_state import DispensedState
from state.atm_state import AtmState

class AuthenticatedState(AtmState):

    def insert_card(self, atm, card): raise IllegalStateException("Session in progress")
    def enter_pin(self, atm, pin): raise IllegalStateException("Already authenticated")

    def withdraw(self, atm:Atm , amount):

      if amount <= 0 or amount % 100 != 0 :
         raise InvalidAmountException(amount)

      if not atm.dispenser.can_dispense(amount):
         raise InsufficientCashException()

      atm.bank.debit(atm.card.account_id,amount)

      atm._set_pending_amount(amount)
      atm._set_state(DispensedState())

    def check_balance(self, atm):
        return atm.bank.get_balance(atm.card.account_id)

    def eject_card(self, atm):
        from state.idle_state import IdleState

        atm._return_card()
        atm._set_state(IdleState())

