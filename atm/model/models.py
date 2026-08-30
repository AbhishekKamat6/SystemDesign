
from dataclasses import dataclass
from datetime import date


# single card can be linked to multiple accounts , current card can have savings account and current account
@dataclass(frozen=True)
class Card:
    card_number : str
    account_id : str
    expiry : date

    def is_expired(self)->bool:
        return self.expiry < date.today()

class Account:

    def __init__(self,account_id:str,balance:int):
        self.account_id = account_id
        self._balance = balance
        self._daily_used = 0


    @property
    def balance(self):
        return self._balance

    @property
    def daily_used(self):
        return self._daily_used

    @balance.setter
    def balance(self,value):
        self._balance = value

    @daily_used.setter
    def daily_used(self,value):
        self._daily_used = value
    
        