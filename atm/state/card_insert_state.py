
from __future__ import annotations

from typing import TYPE_CHECKING

from model.models import Card
from exception.exceptions import IllegalStateException , CardBlockedException , InvalidPinException
from state.authenticate_state import AuthenticatedState 
from state.atm_state import AtmState

if TYPE_CHECKING:
     from atm import Atm

class CardInsertedState(AtmState):

    def __init__(self):
        self.attempts = 0


    def insert_card(self, atm , card ):
          raise IllegalStateException("A card is already inside")

    def enter_pin(self,atm:Atm,pin):
         if atm.bank.verify_pin(atm.card,pin):
              atm._set_state(AuthenticatedState())
              return 
         self.attempts += 1

         if self.attempts >= 3:
              from state.idle_state import IdleState

              atm._retain_card()
              atm._set_state(IdleState())
              return CardBlockedException()

         print(f"Invalid PIN. Attempts remaining: {3-self.attempts}")

    def withdraw(self, atm, amount): raise IllegalStateException("Enter your PIN first")

    def check_balance(self, atm): raise IllegalStateException("Enter your PIN first")

    def eject_card(self,atm:Atm):
         from state.idle_state import IdleState

         atm._return_card()
         atm._set_state(IdleState())