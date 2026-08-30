from state.atm_state import AtmState
from model.models import Card
from exception.exceptions import CardExpiredException,IllegalStateException
from state.card_insert_state import CardInsertedState

class IdleState(AtmState):

    def insert_card(self, atm, card:Card):

        if card.is_expired():
            raise CardExpiredException()

        atm._set_card(card)
        atm._set_state(CardInsertedState())

    def enter_pin(self, atm, pin): raise IllegalStateException("Insert a card first")
    def withdraw(self, atm, amount): raise IllegalStateException("Insert a card first")
    def check_balance(self, atm): raise IllegalStateException("Insert a card first")
    def eject_card(self, atm): raise IllegalStateException("No card inside")