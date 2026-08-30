from abc import ABC,abstractmethod
from model.models import Card

class AtmState(ABC):

    @abstractmethod
    def insert_card(self, atm , card:Card):
        pass

    @abstractmethod
    def enter_pin(self, atm , pin:str ):
        pass

    @abstractmethod
    def withdraw(self, atm , amount:int ):
        pass

    @abstractmethod
    def eject_card(self,atm):
        pass