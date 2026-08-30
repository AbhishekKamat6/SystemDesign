from bank.bank_service import BankService
from cash.cash_dispenser import CashDispenser
from state.idle_state import IdleState
from model.models import Card
from state.atm_state import AtmState

# one instance per active customer session . The CashDispenser passed in should be a SHARED singleton
class Atm:

     def __init__(self, bank:BankService , dispenser:CashDispenser):
          self._state = IdleState()
          self.bank = bank
          self.dispenser = dispenser
          self.card : Card | None = None
          self.pending_amount : int = 0
          self._last_dispensed_notes : dict = {}

      # custom facing
     def insert_card(self , card:Card ) : self._state.insert_card(self,card)

     def enter_pin(self , pin:str) : self._state.enter_pin(self,pin)

     def withdraw(self, amount:int) : self._state.withdraw(self,amount)

     def check_balance(self) -> int : return self._state.check_balance(self)

     def eject_card(self): self._state.eject_card(self)

     # callbacks used by states

     def _set_state(self , s:AtmState) : self._state = s

     def _set_card(self, c:Card): self.card = c

     def _set_pending_amount(self, a:int ): self.pending_amount = a

     def _return_card(self):
          self.card = None
          self.pending_amount = 0

     def _retain_card(self):
          self.card = None
          self.pending_amount = 0

     @property
     def state_name(self)->str:
           return type(self._state).__name__

     @property
     def last_dispensed_notes(self)->dict:
           return self._last_dispensed_notes

        
          