
from abc import ABC , abstractmethod
from model.models import Card

class BankService(ABC):

    @abstractmethod
    def verify_pin(self,card:Card,pin:str) -> bool :
        pass

    @abstractmethod
    def get_balance(self,account_id:str)->str:
        pass

    @abstractmethod
    def debit(self,account_id:str,amount:int) -> None :
        pass

    @abstractmethod
    def credit(self,account_id:str,amount:int)-> None:
        pass